
import os
import gc
import argparse
import re

from crewai import Crew, Process

from agents.scout_agent import create_scout_agent
from agents.synthesis_agent import create_synthesis_agent
from agents.strategy_agent import create_strategy_agent

from tasks.scout_task import create_scout_task
from tasks.synthesis_task import create_synthesis_task
from tasks.strategy_task import create_strategy_task

from tools.web_search import WebSearchTool


def save_report(file_path, report):
    """Save an agent's report to a Markdown file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)


def safe_folder_name(name):
    """Convert a company name into a safe folder name."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def collect_research_evidence(companies):
    """Collect search evidence only for selected companies."""
    search_tool = WebSearchTool()
    evidence_sections = []

    for company in companies:
        queries = [
            f"{company} CRM product updates 2026",
            f"{company} CRM pricing changes 2026",
        ]

        print(f"\nSearching for {company}...")

        for query in queries:
            print(f"  Query: {query}")
            results = search_tool._run(query)

            evidence_sections.append(
                f"COMPANY: {company}\n"
                f"QUERY: {query}\n"
                f"SEARCH RESULTS:\n{results}"
            )

    return "\n\n".join(evidence_sections)


def main(selected_competitor="All Competitors", scout_only=False):
    # --------------------------------------------------
    # PROJECT SETTINGS
    # --------------------------------------------------
    industry = "CRM Software"
    focal_company = "Zoho CRM"
    all_competitors = ["Salesforce", "HubSpot", "Freshworks"]
    region = "Global"
    research_period = "2026"

    run_scout_only = scout_only

    if selected_competitor == "All Competitors":
        competitors = all_competitors
        output_dir = "outputs"
    else:
        if selected_competitor not in all_competitors:
            raise ValueError("Invalid competitor selected.")

        competitors = [selected_competitor]
        output_dir = os.path.join(
            "outputs",
            "comparisons",
            safe_folder_name(selected_competitor)
        )

    os.makedirs(output_dir, exist_ok=True)

    scout_path = os.path.join(output_dir, "scout_report.md")
    synthesis_path = os.path.join(output_dir, "synthesis_report.md")
    strategy_path = os.path.join(output_dir, "strategy_report.md")
    evidence_path = os.path.join(output_dir, "search_evidence.md")

    companies_to_search = [focal_company] + competitors

    print("\n" + "=" * 60)
    print("B2B COMPETITIVE INTELLIGENCE SYSTEM")
    print("=" * 60)
    print(f"Focal Company: {focal_company}")
    print(f"Competitors: {', '.join(competitors)}")
    print(f"Region: {region}")
    print(f"Research Period: {research_period}")
    print(f"Output Folder: {output_dir}")
    print(f"Scout-only mode: {run_scout_only}")

    # --------------------------------------------------
    # STAGE 1: COLLECT RESEARCH EVIDENCE
    # --------------------------------------------------
    print("\nSTAGE 1: COLLECTING RESEARCH EVIDENCE")
    print("-" * 60)

    research_evidence = collect_research_evidence(
        companies_to_search
    )

    save_report(evidence_path, research_evidence)
    print(f"\nSearch evidence saved to {evidence_path}")

    # --------------------------------------------------
    # STAGE 2: SCOUT AGENT
    # --------------------------------------------------
    print("\nSTAGE 2: SCOUT AGENT")
    print("-" * 60)

    scout = create_scout_agent()

    scout_task = create_scout_task(
        agent=scout,
        industry=industry,
        focal_company=focal_company,
        competitors=competitors,
        region=region,
        research_period=research_period,
        research_evidence=research_evidence
    )

    scout_crew = Crew(
        agents=[scout],
        tasks=[scout_task],
        process=Process.sequential,
        verbose=True
    )

    scout_result = scout_crew.kickoff()
    scout_report = str(scout_result)

    save_report(scout_path, scout_report)
    print(f"\nScout Agent completed. Report saved to {scout_path}")

    del scout_crew, scout_task, scout_result, scout
    gc.collect()

    if run_scout_only:
        print("\nScout-only run completed.")
        print(f"Scout report: {scout_path}")
        print(f"Search evidence: {evidence_path}")
        return

    # --------------------------------------------------
    # STAGE 3: SYNTHESIS AGENT
    # --------------------------------------------------
    print("\nSTAGE 3: SYNTHESIS AGENT")
    print("-" * 60)

    synthesis = create_synthesis_agent()

    synthesis_task = create_synthesis_task(
        agent=synthesis,
        scout_report=scout_report
    )

    synthesis_crew = Crew(
        agents=[synthesis],
        tasks=[synthesis_task],
        process=Process.sequential,
        verbose=False
    )

    synthesis_result = synthesis_crew.kickoff()
    synthesis_report = str(synthesis_result)

    save_report(synthesis_path, synthesis_report)
    print(
        f"\nSynthesis Agent completed. "
        f"Report saved to {synthesis_path}"
    )

    del synthesis_crew, synthesis_task, synthesis_result, synthesis
    gc.collect()

    # --------------------------------------------------
    # STAGE 4: STRATEGY AGENT
    # --------------------------------------------------
    print("\nSTAGE 4: STRATEGY AGENT")
    print("-" * 60)

    strategy = create_strategy_agent()

    strategy_task = create_strategy_task(
        agent=strategy,
        synthesis_report=synthesis_report,
        focal_company=focal_company,
        industry=industry,
        region=region
    )

    strategy_crew = Crew(
        agents=[strategy],
        tasks=[strategy_task],
        process=Process.sequential,
        verbose=False
    )

    strategy_result = strategy_crew.kickoff()
    strategy_report = str(strategy_result)

    save_report(strategy_path, strategy_report)

    print(
        f"\nStrategy Agent completed. "
        f"Report saved to {strategy_path}"
    )

    del strategy_crew, strategy_task, strategy_result, strategy
    gc.collect()

    # --------------------------------------------------
    # PIPELINE COMPLETION
    # --------------------------------------------------
    print("\n" + "=" * 60)
    print("ALL STAGES COMPLETED")
    print("=" * 60)

    print("\nGenerated Reports:")
    print(evidence_path)
    print(scout_path)
    print(synthesis_path)
    print(strategy_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="B2B Competitive Intelligence System"
    )

    parser.add_argument(
        "--competitor",
        choices=[
            "Salesforce",
            "HubSpot",
            "Freshworks",
            "All Competitors"
        ],
        default="All Competitors",
        help="Select a competitor or run analysis for all."
    )

    parser.add_argument(
        "--scout-only",
        action="store_true",
        help="Run only the Scout agent."
    )

    args = parser.parse_args()
    main(args.competitor, scout_only=args.scout_only)
