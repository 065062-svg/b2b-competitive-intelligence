
from crewai import Task


def create_synthesis_task(agent, scout_report):
    return Task(
        description=f"""
Analyze and consolidate the competitive intelligence collected
by the Scout Agent.

SCOUT RESEARCH REPORT:
{scout_report}

OBJECTIVE:
Create an evidence-based comparative intelligence report
using only the information in the Scout Research Report.

YOUR RESPONSIBILITIES:

1. COMPETITOR PROFILES
   - Organize findings separately for each competitor included
     in the Scout Report.
   - Do not introduce additional competitors.
   - Summarize only documented products, features, pricing,
     launches, updates, and expansion activities.

2. COMPARATIVE FEATURE MATRIX
   Compare competitors using the available evidence for:
   - Products and features
   - Pricing and commercial strategies
   - Product launches and updates
   - Market expansion
   - Emerging trends

   Use "Not found in Scout Report" when evidence is unavailable.
   Do not assume that missing information means a competitor
   does not offer a feature or activity.

3. KEY MARKET PATTERNS
   - Identify similarities and differences supported by
     the Scout Report.
   - Separate documented facts from analytical observations.
   - Clearly label any interpretation as analysis.

4. INFORMATION GAPS
   - Identify competitors, categories, or time periods
     for which sufficient verified evidence is unavailable.
   - Do not describe missing research as a confirmed
     competitive weakness.
   - Highlight any findings with incomplete dates,
     unclear evidence, or missing source URLs.

5. SOURCE VALIDATION
   - Retain the source URLs provided in the Scout Report.
   - Associate each finding with its relevant source.
   - Do not invent, modify, or claim to have verified URLs.
   - Do not add external facts or sources.

6. EVIDENCE DISCIPLINE
   - Use only information contained in the Scout Report.
   - Do not invent prices, features, market shares,
     customer numbers, launches, or company activities.
   - Do not convert assumptions into facts.
   - If competitors have unequal evidence coverage,
     explicitly disclose this limitation.
   - Do not force a comparison when the available evidence
     is insufficient.

7. RELEVANCE TO THE FOCAL COMPANY
   - Explain the potential competitive implications for
     the focal company only where the Scout Report
     supports the underlying facts.
   - Clearly distinguish evidence from interpretation.
   - Do not provide final strategic recommendations;
     those belong to the Strategy Agent.

REPORTING RULE:
Every factual claim must be traceable to the Scout Report.
If a claim cannot be supported by it, omit the claim or
identify the information as unavailable.

""",
        expected_output="""
A structured, evidence-based competitive intelligence
synthesis report containing:

1. Executive summary
2. Research scope and evidence limitations
3. Individual competitor profiles
4. Comparative feature matrix
5. Key similarities and differences
6. Evidence-supported market patterns
7. Potential implications for the focal company,
   clearly labelled as analysis
8. Information gaps and unverified details
9. Source URLs associated with relevant findings

Use "Not found in Scout Report" wherever evidence
is unavailable.

Do not invent facts, add competitors, or make
unsupported comparative conclusions.
""",
        agent=agent
    )
