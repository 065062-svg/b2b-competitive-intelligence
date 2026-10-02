
from crewai import Task


def create_strategy_task(agent, synthesis_report, focal_company, industry, region):
    return Task(
        description=f"""
Prepare an evidence-based executive strategic intelligence brief
using the Synthesis Report provided below.

Focal Company: {focal_company}
Industry: {industry}
Region: {region}

SYNTHESIS REPORT:
{synthesis_report}

OBJECTIVE:
Develop practical strategic options for {focal_company}
based only on the documented findings in the Synthesis Report.

EVIDENCE RULES:
1. Use only facts supported by the Synthesis Report.
2. Do not invent company capabilities, prices, market shares,
   customer data, competitor activities, or market conditions.
3. Do not treat missing information as proof that a weakness,
   threat, or competitive gap exists.
4. Clearly separate:
   - Verified facts
   - Strategic analysis and interpretation
   - Proposed actions and recommendations
5. If the evidence is insufficient, identify the information
   gap and state what should be validated before acting.
6. Do not introduce new competitors or unsupported sources.

1. SWOT ANALYSIS

Strengths:
Identify documented internal capabilities, product features,
resources, or advantages of the focal company.
Do not infer strengths solely from missing competitor data.

Weaknesses:
Include only documented internal limitations or shortcomings.
Do not classify a lack of research, missing competitor data,
or an unverified assumption as a company weakness.

Opportunities:
Identify evidence-supported external market developments
that could create opportunities for the focal company.
You may suggest potential opportunities as hypotheses, but
clearly label them as hypotheses requiring validation.

Threats:
Identify documented competitor actions, market changes,
or external risks supported by the Synthesis Report.
Clearly distinguish established evidence from potential risks
that require further validation.

2. COMPETITIVE GAPS AND MARKET OPPORTUNITIES
- Identify competitive gaps only when supported by evidence.
- Explain which findings indicate a potential opportunity.
- Label unverified gaps as research questions, not facts.
- Avoid claims of market leadership or market share
  without supporting evidence.

3. TARGET CUSTOMER SEGMENTS AND POSITIONING
- Suggest relevant customer segments only where supported
  by the available evidence.
- Clearly label proposed segments and positioning as
  strategic options rather than confirmed company strategies.
- Do not claim that the company already serves a segment
  unless the report supports that claim.

4. ACTIONABLE GO-TO-MARKET (GTM) RECOMMENDATIONS
For each recommendation, provide:
- Proposed action
- Evidence supporting the recommendation
- Strategic rationale
- Intended customer segment, if supported
- Expected business outcome, expressed as a hypothesis
  where it has not been measured
- Key implementation considerations
- Risks and validation required

Do not invent numerical targets, budgets, or expected
revenue improvements.

5. STRATEGIC PRIORITIES FOR THE NEXT 6-12 MONTHS
Suggest a practical sequence of proposed actions.
For each priority, explain:
- Why it is being proposed
- Supporting evidence or identified information gap
- Suggested time horizon
- A measurable indicator to track, if appropriate

Clearly identify these as proposed priorities, not
announced or existing company commitments.

6. RISKS AND MITIGATION
- Identify evidence-supported risks.
- Separate documented risks from potential risks.
- Propose practical mitigation measures.
- Do not present general industry risks as confirmed
  company-specific problems.

7. SUPPORTING EVIDENCE AND INFORMATION GAPS
- Connect factual claims to findings and sources
  included in the Synthesis Report.
- Do not invent or alter source URLs.
- Clearly list the important information that is missing.
- Explain how missing evidence limits the analysis.

FINAL REQUIREMENT:
The brief must distinguish what is known, what is inferred,
and what is being recommended. Do not force a SWOT category
or recommendation when the evidence does not support it.
Prioritize transparency, practicality, and traceability.
""",
        expected_output="""
An executive strategic intelligence brief containing:

1. Executive summary
2. Research scope and evidence limitations
3. Evidence-based SWOT analysis
4. Competitive gaps and market opportunities
5. Proposed target customer segments and positioning
6. Actionable GTM recommendations with supporting rationale
7. Proposed 6-12 month strategic priorities
8. Risks and possible mitigation measures
9. Supporting evidence and information gaps

Clearly distinguish verified facts, strategic interpretations,
hypotheses, and recommendations.

Do not invent company data, competitor actions, or
unsupported market conclusions.
""",
        agent=agent
    )
