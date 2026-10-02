
from crewai import Task


def create_scout_task(
    agent,
    industry,
    focal_company,
    competitors,
    region,
    research_period,
    research_evidence
):
    all_companies = [focal_company] + competitors

    return Task(
        description=f"""
You are a B2B competitive intelligence researcher.

Analyse the following collected web-search evidence
for companies in the {industry} industry:

Companies: {", ".join(all_companies)}
Region: {region}
Research period: {research_period}
Focal company: {focal_company}

Collected research evidence:
{research_evidence}

Use only the evidence provided. Organize findings
separately for each company.

For each company, report:
- Product updates and launches
- Pricing information, if available
- Partnerships and market developments
- Source titles and URLs
- Information gaps and limitations

Distinguish sourced facts from analysis.
Do not invent details or make strategic recommendations.
If evidence for a company is missing, state that clearly.
""",
        expected_output=(
            "A concise, evidence-based competitive intelligence "
            "report for each company, with source titles, URLs, "
            "and information gaps."
        ),
        agent=agent
    )
