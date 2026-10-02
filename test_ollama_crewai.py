from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(
    model="ollama/qwen2.5:3b",
    base_url="http://localhost:11434"
)

scout = Agent(
    role="B2B Market Research Scout",
    goal="Explain competitive intelligence for B2B marketing",
    backstory="You are a market research analyst who studies competitors.",
    llm=llm,
    verbose=True
)

task = Task(
    description="Explain competitive intelligence in B2B marketing in 3 concise sentences.",
    expected_output="A clear explanation in 3 sentences.",
    agent=scout
)

crew = Crew(
    agents=[scout],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
print("\n--- RESULT ---")
print(result)
