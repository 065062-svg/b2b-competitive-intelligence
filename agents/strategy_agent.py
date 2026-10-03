import os
from crewai import Agent, LLM


def create_strategy_agent():
    llm = LLM(
        model="ollama/qwen2.5:3b",
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.2
    )

    strategy_agent = Agent(
        role="B2B Marketing and Corporate Strategy Analyst",
        goal=(
            "Develop an evidence-based SWOT analysis and actionable "
            "go-to-market strategy using competitive intelligence."
        ),
        backstory=(
            "You are a B2B corporate strategy analyst who translates "
            "market research into executive insights. You identify "
            "strategic opportunities, business risks, competitive "
            "gaps, and practical go-to-market options. You distinguish "
            "verified facts from analysis and avoid unsupported claims."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        max_iter=3
    )

    return strategy_agent
