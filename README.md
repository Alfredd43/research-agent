# AI-Powered Research Assistant

A modular, extensible platform that automates academic research using advanced LLM agents and free APIs. Ideal for capstone projects, portfolios, and research demos.

## Features
- Automates literature search, summarization, and citation extraction
- Identifies research gaps, trends, and generates novel ideas
- Organizes workflow and creates custom reading plans
- No OpenAI costs: leverages Cohere and free APIs (Semantic Scholar, arXiv)
- Modular agent-based architecture for easy extension

## Core Agents
- **LiteratureAgent**: Searches open-access databases (Semantic Scholar, arXiv)
- **SummarizerAgent**: Summarizes papers using Cohere Command-R
- **CitationAgent**: Extracts and formats references (GROBID)
- **InsightAgent**: Detects gaps, contradictions, and trends (embeddings, clustering)
- **IdeaGeneratorAgent**: Proposes new research ideas
- **SchedulerAgent**: Builds weekly research/reading plans

## Architecture
- **Backend**: FastAPI, modular agent system
- **Frontend**: Streamlit UI for interactive research workflow
- **Integrations**: Cohere, Semantic Scholar, arXiv, GROBID, Hugging Face
- **Data Science**: pandas, scikit-learn, matplotlib

## Quickstart
1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Cohere API key to `config/cohere_keys.json`
4. Launch the UI: `streamlit run app/streamlit_ui.py`

## Folder Structure
- `agents/` — Automation agents
- `app/` — Streamlit UI & backend
- `utils/` — API clients, text processing
- `config/` — API keys/configs

## Roadmap
- Chrome extension
- Voice command support
- Notion/Obsidian export
- User feedback loop 