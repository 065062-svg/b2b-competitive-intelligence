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
You are conducting evidence-based B2B competitive intelligence research.

RESEARCH SCOPE:
Industry: {industry}
Focal Company: {focal_company}
Competitors: {", ".join(competitors)}
Region: {region}
Research Period: {research_period}

MAIN OBJECTIVE:
Independently research the companies using your web search
tool and prepare a structured competitive intelligence report.

RESEARCH AUTONOMY:
You have access to the Search CRM market intelligence tool.

MANDATORY TOOL USE:
Before writing the report, you MUST call your web search
tool at least once for each company listed below.
Use a separate, company-specific query for each company.

Do not skip a company just because pre-collected evidence
is available or previous searches returned no results.

For each company:
- Search for product updates or launches within the research period.
- Search for pricing, partnerships or market developments
  when relevant and within the available tool-call limit.
- Use the returned search results as evidence.
- If the tool returns an error or no results, state that
  the search did not return usable evidence.
- Never claim a tool was used if no tool call occurred.

The pre-collected research evidence below is a starting
point only. It does not replace the mandatory tool calls.
You may use it alongside your own tool-based searches.

RESEARCH INSTRUCTIONS:

1. Create a separate section for each company:
   {", ".join(all_companies)}

2. Treat {focal_company} as the focal company.
   Include findings for every listed competitor.

3. Investigate:
   - Product launches and product updates
   - Pricing and commercial changes
   - Market entry and geographic expansion
   - Partnerships and strategic developments
   - Other significant company announcements

4. Keep each company's findings strictly separate.
   Never attribute one company's actions to another.

5. Prioritize official company sources.
   Clearly identify third-party sources.
   Do not label a source as official unless its ownership
   is evident from the search result.

6. Focus on developments within {research_period}
   and the specified region: {region}.
   If date or region is unclear, state this limitation.

7. Do not invent findings, prices, dates, URLs,
   product names or company actions.

8. Distinguish clearly between:
   - Facts supported by search results
   - Analytical observations based on those facts
   - Details that remain unverified

9. Search-result snippets are not full-page verification.
   Never claim to have read a complete webpage unless
   the tool actually retrieved and verified its contents.

10. A title mentioning a company does not automatically
    validate every claim in its summary.
    Check relevance to the company and product.

11. If attribution is unclear, mark the claim
    as unverified or exclude it.

12. Missing search results do not prove that
    a company has taken no action.

13. Do not make unsupported estimates or assumptions.

14. Do not make strategic recommendations.
    Those belong to the Strategy Agent.

15. Avoid unnecessary repeated searches.
    Use focused queries and prioritize relevant evidence.

PRE-COLLECTED RESEARCH EVIDENCE:
{research_evidence}

REPORT REQUIREMENTS:

For each company, include:
- Company name
- Finding category
- Development or "No verified finding identified"
- Concise evidence summary
- Date or period, if available
- Region, if available
- Source title and URL
- Source type: official or third-party
- Verification status
- Relevance to {focal_company}

SOURCE QUALITY:
- Prefer official company sources.
- Identify third-party sources clearly.
- Report source disagreements without unsupported resolution.
- Do not describe a claim as confirmed without evidence.

COVERAGE:
Every company must have its own section, even if
no verified findings are identified.
Identify industry trends only when supported by
multiple relevant findings or sources.
Do not generalize from one announcement.
Do not add competitors outside the supplied list.

Prioritize accurate attribution, evidence quality
and competitor coverage over report length.
""",
        expected_output=f"""
A concise, structured competitive intelligence report
for {industry}, focused on {focal_company} and
its listed competitors.

Organize the report as follows:

1. Research Scope
   - Industry
   - Focal company
   - Competitors
   - Region
   - Research period
   - Research limitations

2. Individual Company Findings
   Separate sections for:
   {", ".join(all_companies)}

   For each finding include:
   - Finding category
   - Development
   - Supporting evidence
   - Date and region, if available
   - Source title and URL
   - Source type
   - Verification status
   - Relevance to {focal_company}

3. Comparative Overview
   Summarize evidence-supported developments.
   Do not rank competitors or invent missing details.

4. Evidence-Supported Industry Trends
   Include only trends supported by relevant findings
   from multiple companies or sources.

5. Information Gaps and Limitations
   Include missing information, unclear attribution,
   unavailable dates and unverified findings.
   Explain that missing results do not prove
   that no company action occurred.

6. Source List
   Group source titles, URLs and source types by company.

Clearly distinguish source-supported facts,
analytical observations and unverified details.
Do not invent information to fill gaps.
""",
        agent=agent
    )