# 🧠 AI-Powered Research Assistant (Cohere & Free APIs)

- Automates academic research using modular LLM agents
- Finds, summarizes, and extracts citations from research papers
- Identifies research gaps, trends, and suggests new ideas
- Organizes workflow and creates custom reading plans
- No OpenAI costs: uses Cohere + free APIs (Semantic Scholar, arXiv)
- Modular, extensible, and perfect for capstone/portfolio/demo

## Key Agents
- **LiteratureAgent**: Searches open databases (Semantic Scholar/arXiv)
- **SummarizerAgent**: Summarizes papers using Cohere Command-R
- **CitationAgent**: Extracts and formats references (GROBID)
- **InsightAgent**: Finds gaps, contradictions, trends (embeddings, clustering)
- **IdeaGeneratorAgent**: Suggests novel research ideas
- **SchedulerAgent**: Creates weekly research/reading plans

## Tech Stack
- Cohere Command-R+, LangChain/AutoGen, Streamlit, FastAPI
- Semantic Scholar API, arXiv API, GROBID
- pandas, scikit-learn, matplotlib, Hugging Face

## Setup
- Clone repo & install requirements: `pip install -r requirements.txt`
- Add Cohere API key to `config/cohere_keys.json`
- Run Streamlit UI: `streamlit run app/streamlit_ui.py`

## Folder Structure
- `agents/` — All automation agents
- `app/` — Streamlit UI & backend logic
- `utils/` — API clients, text cleaning
- `config/` — API keys/configs

## Future Ideas
- Chrome extension, voice commands, Notion/Obsidian export, user feedback loop 