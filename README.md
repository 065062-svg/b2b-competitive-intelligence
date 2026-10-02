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
## System Architecture

The workflow is organized into three AI-agent stages, supported by Python-based web research.

```text
User
  |
  v
Python Research Precollection
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
```

### Workflow Overview

1. **Research Precollection:** Python runs web searches for competitor product updates and pricing information.
2. **Scout Agent:** Organizes the collected evidence into company-wise competitive intelligence findings.
3. **Synthesis Agent:** Consolidates the findings into a comparative analysis.
4. **Strategy Agent:** Develops strategic insights, including SWOT and go-to-market recommendations.
5. **Output:** The reports are saved in Markdown format in the `outputs/` folder.

The current main workflow uses precollected search evidence. Although a web-search tool is configured for the Scout agent, the main pipeline currently relies on Python's fixed search queries.
## Technology Stack

- **Python:** Core programming language and workflow execution
- **CrewAI:** Multi-agent orchestration
- **Ollama:** Local language model runtime
- **Qwen 2.5 3B:** Configured language model
- **DuckDuckGo Search:** Web-search capability
- **Streamlit:** Interactive dashboard
- **Markdown:** Generated reports

## Project Structure

```text
b2b_competitive_intelligence/
├── agents/
│   ├── scout_agent.py
│   ├── synthesis_agent.py
│   └── strategy_agent.py
├── config/
│   └── settings.py
├── data/
├── outputs/
│   ├── search_evidence.md
│   ├── scout_report.md
│   ├── synthesis_report.md
│   └── strategy_report.md
├── tasks/
│   ├── scout_task.py
│   ├── scout_task_backup.py
│   ├── synthesis_task.py
│   └── strategy_task.py
├── tools/
│   ├── crew_search_tool.py
│   ├── web_search.py
│   └── webpage_extractor.py
├── app.py
├── main.py
├── requirements.txt
└── README.md
```
## Requirements

- Python 3.10 or later
- Ollama installed and running
- The `qwen2.5:3b` model available in Ollama
- Dependencies listed in `requirements.txt`

## Setup and Installation

### 1. Navigate to the project directory

```bash
cd ~/mba_agent_lab/b2b_competitive_intelligence
```

### 2. Activate the virtual environment

```bash
source ~/mba_agent_lab/venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Ensure Ollama is running

Make sure Ollama is accessible at `http://localhost:11434` and the configured model is available.

```bash
ollama pull qwen2.5:3b
```

### 5. Configure environment variables

Review the `.env` file if environment variables are required. Keep API keys and other secrets private, and do not upload them to GitHub.
## Running the Application

### Run the full workflow

```bash
python main.py
```

This runs the research precollection stage, followed by the Scout, Synthesis, and Strategy agents sequentially.

### Run Scout for a single competitor

```bash
python main.py --competitor Freshworks --scout-only
```

This collects evidence and runs the Scout stage for the selected competitor.

### Launch the Streamlit dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the dashboard. Select competitors and start the research workflow through the interface.

## Generated Outputs

The system saves its reports in the `outputs/` directory.

| File | Description |
|---|---|
| `search_evidence.md` | Web-search results collected before agent analysis |
| `scout_report.md` | Company-wise competitive intelligence findings |
| `synthesis_report.md` | Consolidated competitor comparison and key findings |
| `strategy_report.md` | Strategic analysis and go-to-market recommendations |
## Research Reliability and Limitations

- The current research precollection uses fixed search queries for product updates and pricing.
- Search-result snippets may not provide enough detail to verify every claim.
- Pricing can vary by region, subscription plan, billing frequency, and date.
- AI-generated reports may contain inaccurate, incomplete, or misattributed information. Verify important claims against original sources, preferably official company websites.
- The main workflow uses precollected evidence rather than relying on fully autonomous agent-led research.
- The local language model is relatively small, so complex tasks may produce incomplete results.

The system is a research and decision-support prototype. Human review is necessary before using its findings in business decisions or academic presentations.

## Suggested Demonstration Flow

1. Launch the Streamlit dashboard.
2. Select the CRM competitors to analyze.
3. Start the research workflow.
4. Review the collected search evidence.
5. Open the Scout report to see company-wise findings.
6. Review the Synthesis report for competitor comparisons.
7. Present the Strategy report and discuss its SWOT and go-to-market insights.
8. Explain the importance of validating generated findings against original sources.

## Academic Use

This project demonstrates how web research, local language models, and multi-agent orchestration can support competitive intelligence and strategic marketing analysis. Generated findings should be reviewed and validated before submission or presentation.