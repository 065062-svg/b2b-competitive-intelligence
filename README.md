# Automated B2B Competitive Intelligence & Market Scouting System

A multi-agent competitive intelligence project developed for Strategic Marketing & Corporate Strategy. The system collects web-search evidence about CRM providers and uses AI agents to organize findings, compare competitors, and develop strategic recommendations.

## Project Objective

Monitor the CRM software market to identify product updates, pricing information, partnerships, and market developments.

- **Industry:** CRM software
- **Focal company:** Zoho CRM
- **Competitors:** Salesforce, HubSpot, Freshworks
- **Research scope:** Global
- **Research period:** 2026

## Key Features

- Web-search evidence collection for selected CRM competitors
- Company-wise competitive intelligence reports
- Consolidated competitor analysis
- SWOT and go-to-market strategic recommendations
- Streamlit dashboard for running the workflow
- Markdown reports for review and download
- Multi-agent orchestration using CrewAI
- Local language model execution through Ollama
- Docker-based application deployment

## System Architecture

The workflow is organized into three AI-agent stages, supported by Python-based web research.

```text
                         User
                          |
                          v
                 Streamlit Dashboard
                          |
                          v
                Python Orchestration
                          |
                          v
              Research Precollection
                          |
                          v
              Collected Search Evidence
                          |
                          v
                    Scout Agent
                          |
                          v
                   Scout Report
                          |
                          v
                  Synthesis Agent
                          |
                          v
                 Synthesis Report
                          |
                          v
                  Strategy Agent
                          |
                          v
                  Strategy Report
                          |
                          v
                 Markdown Outputs
```

### Workflow Overview

1. **Research Precollection:** Python runs web searches for competitor product updates and pricing information.
2. **Scout Agent:** Organizes the collected evidence into company-wise competitive intelligence findings.
3. **Synthesis Agent:** Consolidates the findings into a comparative analysis.
4. **Strategy Agent:** Develops strategic insights, including SWOT and go-to-market recommendations.
5. **Output:** The reports are saved in Markdown format in the `outputs/` folder.

The current main workflow uses precollected search evidence. Although a web-search tool is configured for the Scout agent, the main pipeline currently relies on Python's fixed search queries.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language and workflow execution |
| CrewAI | Multi-agent orchestration |
| Ollama | Local language model runtime |
| Qwen 2.5 3B | Configured language model |
| DuckDuckGo Search | Web-search capability |
| Streamlit | Interactive dashboard |
| Docker | Application containerization |
| Docker Compose | Application deployment and configuration |
| Markdown | Generated reports |

## Project Structure

```text
b2b_competitive_intelligence/
├── agents/
│   ├── scout_agent.py
│   ├── synthesis_agent.py
│   └── strategy_agent.py
├── config/
│   └── settings.py
├── outputs/
│   ├── search_evidence.md
│   ├── scout_report.md
│   ├── synthesis_report.md
│   ├── strategy_report.md
│   └── comparisons/
├── tasks/
│   ├── scout_task.py
│   ├── scout_task_backup.py
│   ├── scout_task_original.py
│   ├── synthesis_task.py
│   └── strategy_task.py
├── tools/
│   ├── crew_search_tool.py
│   ├── web_search.py
│   └── webpage_extractor.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── app.py
├── main.py
├── requirements.txt
├── test_ollama_crewai.py
└── README.md
```

## Requirements

- Python 3.10 or later for local execution
- Docker and Docker Compose for containerized execution
- Ollama installed and running
- The `qwen2.5:3b` model available in Ollama
- Dependencies listed in `requirements.txt`
- Sufficient memory to run the local language model and application

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/065062-svg/b2b-competitive-intelligence.git
cd b2b-competitive-intelligence
```

### 2. Set up Ollama

Install Ollama from the official website:

https://ollama.com/

Pull the configured model:

```bash
ollama pull qwen2.5:3b
```

Ensure Ollama is running and accessible at:

```text
http://localhost:11434
```

The application uses a locally hosted model through Ollama, rather than requiring a paid cloud-based LLM API.

### 3. Local Python setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, activate the environment using:

```powershell
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Environment configuration

The current application does not require a `.env` file for its default configuration. Ollama connection settings are configured in the application and Docker Compose setup.

Do not commit API keys, credentials, or other sensitive configuration values to GitHub.

## Running the Application

### Option 1: Run the full workflow locally

Ensure Ollama is running and the required model is available.

Run:

```bash
python main.py
```

This executes the research precollection stage, followed by the Scout, Synthesis, and Strategy agents sequentially.

### Run Scout for a single competitor

```bash
python main.py --competitor Freshworks --scout-only
```

This collects evidence and runs the Scout stage for the selected competitor.

The supported competitor options are:

- Salesforce
- HubSpot
- Freshworks
- All Competitors

### Launch the Streamlit dashboard locally

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, typically:

```text
http://localhost:8501
```

Select the competitors and start the research workflow through the dashboard interface.

### Option 2: Run with Docker Compose

Ensure Docker is installed and running, and that Ollama is running on the host machine with the required model available.

Build and start the application:

```bash
docker compose up -d --build
```

Check the running container:

```bash
docker compose ps
```

Open the dashboard in a browser:

```text
http://localhost:8501
```

View application logs:

```bash
docker compose logs -f app
```

Stop the application:

```bash
docker compose down
```

**Note:** The Dockerized application connects to Ollama running on the host through `host.docker.internal`. The current Docker Compose configuration includes a host gateway mapping for this connection. The Ollama service itself is not containerized by this project.

## Generated Outputs

The system saves its reports in the `outputs/` directory.

| File | Description |
|---|---|
| `search_evidence.md` | Web-search results collected before agent analysis |
| `scout_report.md` | Company-wise competitive intelligence findings |
| `synthesis_report.md` | Consolidated competitor comparison and key findings |
| `strategy_report.md` | Strategic analysis and go-to-market recommendations |
| `comparisons/` | Directory for comparison-related outputs, when generated |

Reports are saved in Markdown format so that they can be reviewed, downloaded, and used in presentations or further analysis.

## Research Reliability and Limitations

- The current research precollection uses fixed search queries for product updates and pricing.
- Search-result snippets may not provide enough detail to verify every claim.
- Pricing can vary by region, subscription plan, billing frequency, and date.
- AI-generated reports may contain inaccurate, incomplete, or misattributed information. Verify important claims against original sources, preferably official company websites.
- The main workflow uses precollected evidence rather than relying on fully autonomous agent-led research.
- The configured Scout web-search tool does not mean every finding is independently verified against a full webpage.
- The local language model is relatively small, so complex tasks may produce incomplete results.
- Strategic recommendations are generated from the available research and should be treated as proposals for human review.

The system is a research and decision-support prototype. Human review is necessary before using its findings in business decisions or academic presentations.

## Suggested Demonstration Flow

The following sequence can be used for a five-minute project demonstration:

1. **Introduction:** Explain the business problem and the objective of automating competitive intelligence in the CRM software market.
2. **Dashboard:** Launch the Streamlit dashboard and select the competitors to analyze.
3. **Research Precollection:** Show how Python collects search evidence for the selected CRM providers.
4. **Scout Agent:** Demonstrate how the Scout agent organizes the collected evidence into company-wise findings.
5. **Synthesis Agent:** Explain how the Synthesis agent consolidates the Scout findings into a comparative analysis.
6. **Strategy Agent:** Present the generated SWOT analysis, competitive gaps, and go-to-market recommendations.
7. **Outputs and Logs:** Open the generated Markdown reports and show the available execution logs to explain the workflow and agent handoffs.
8. **Limitations:** Briefly explain why AI-generated findings and recommendations require verification against original sources.

Where available, include a genuine tool execution trace and an example of error handling or recovery. Do not present simulated logs or claim that an error was recovered unless it was actually demonstrated.

## Academic Use

This project demonstrates how web research, local language models, and multi-agent orchestration can support competitive intelligence and strategic marketing analysis.

The system is intended as an academic research and decision-support prototype. Generated findings and strategic recommendations should be reviewed and validated before submission or presentation.
