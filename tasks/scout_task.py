
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

Analyse the collected web-search evidence for companies
in the {industry} industry.

Companies: {", ".join(all_companies)}
Region: {region}
Research period: {research_period}
Focal company: {focal_company}

Collected research evidence:
{research_evidence}

RESEARCH RULES:
1. Use only the collected evidence. Do not invent facts,
   dates, prices, partnerships, or product updates.
2. Do not treat a lack of search results as proof that
   a company has made no updates or pricing changes.
3. Clearly classify findings as:
   - Supported by the provided evidence
   - Unverified or insufficiently supported
   - No relevant evidence found in the searches
4. Distinguish current listed prices from confirmed
   pricing changes. Claim a price change only when
   evidence supports a comparison with an earlier price.
5. Attach the relevant source title and URL to each
   supported finding. Do not attach unrelated sources.
6. If sources conflict, describe the contradiction
   and identify the conflicting evidence.
7. Do not claim that a source or URL was independently
   verified unless the evidence explicitly confirms it.
8. Keep findings within the specified research period.
   If dates are unclear or outside the period, flag this.
9. Separate sourced facts from analysis. Label analysis
   clearly and do not present it as a verified fact.
10. Do not create strategic recommendations.

REPORT STRUCTURE:

For each company, provide:
- Product updates and launches
- Current pricing information, if available
- Confirmed pricing changes, if available
- Partnerships and market developments
- Evidence for each finding, including source title and URL
- Unverified claims and conflicting information
- Information gaps and research limitations

End with a brief evidence-quality summary that identifies
which areas have strong evidence, limited evidence, or
no relevant evidence in the collected searches.

Be concise, factual, and transparent about uncertainty.
Do not infer that missing information means an event
did not occur.
""",
        expected_output=(
            "A structured, evidence-based competitive "
            "intelligence report for each company. Each "
            "finding must be classified by evidence status "
            "and include relevant source titles and URLs. "
            "The report must identify contradictions, "
            "uncertainties, and information gaps."
        ),
        agent=agent
    )
