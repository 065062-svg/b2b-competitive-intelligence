from crewai import Agent, LLM
from tools.crew_search_tool import search_crm_market


def create_scout_agent():
    llm = LLM(
        model="ollama/qwen2.5:3b",
        base_url="http://localhost:11434",
        temperature=0.2
    )

    scout_agent = Agent(
        role="B2B Competitive Intelligence Scout",
        goal=(
            "Research CRM competitors using web search tools to identify "
            "product updates, pricing changes, market expansion, "
            "partnerships, and industry developments. "
            "Ensure accurate source attribution and evidence-based findings."
        ),
        backstory=(
            "You are a B2B competitive intelligence analyst specializing "
            "in CRM software and strategic marketing. You independently "
            "choose relevant web searches, analyze search results, "
            "distinguish source-supported facts from analysis, and identify "
            "information gaps. You never invent findings or claim to have "
            "verified information beyond the evidence available."
        ),
        tools=[search_crm_market],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=8
    )

    return scout_agent
