import os
from crewai import Agent, LLM


def create_synthesis_agent():
    llm = LLM(
        model="ollama/qwen2.5:3b",
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.2
    )

    synthesis_agent = Agent(
        role="B2B Competitive Intelligence Synthesis Analyst",
        goal=(
            "Consolidate web research into a structured competitor "
            "comparison, identify market patterns, and highlight "
            "information gaps."
        ),
        backstory=(
            "You are a strategic market intelligence analyst. "
            "You organize unstructured research, identify duplicate "
            "findings, compare competitors across relevant dimensions, "
            "and distinguish verified facts from missing information. "
            "You never invent facts, prices, or product capabilities."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3
    )

    return synthesis_agent
