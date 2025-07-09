import streamlit as st
import requests
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(
    page_title="AI-Powered Research Assistant",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for modern look
st.markdown(
    """
    <style>
    body, .stApp { background-color: #181825; color: #f5f6fa; }
    .stButton>button { background: #ff4b4b; color: white; border-radius: 8px; font-weight: bold; }
    .stTextInput>div>input, .stTextArea>div>textarea { background: #232336; color: #f5f6fa; border-radius: 8px; }
    .stSelectbox>div>div>div>div { background: #232336; color: #f5f6fa; border-radius: 8px; }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #ff4b4b; }
    .result-panel { background: #232336; border-radius: 12px; padding: 1.5em; margin-top: 1em; color: #f5f6fa; }
    .agent-desc { color: #b3b3b3; font-size: 0.95em; margin-bottom: 1em; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
<h1 style='text-align: center; font-size: 2.5em;'>🧠 AI-Powered Research Assistant</h1>
<p style='text-align: center; color: #b3b3b3;'>Automate your academic workflow with creative AI agents</p>
""", unsafe_allow_html=True)

AGENTS = {
    "LiteratureAgent": {
        "endpoint": "/literature",
        "desc": "🔎 Searches open databases (Semantic Scholar/arXiv) for relevant papers."
    },
    "SummarizerAgent": {
        "endpoint": "/summarize",
        "desc": "📝 Summarizes long academic papers using Cohere Command-R."
    },
    "CitationAgent": {
        "endpoint": "/citation",
        "desc": "🔗 Parses and formats references using GROBID."
    },
    "InsightAgent": {
        "endpoint": "/insight",
        "desc": "🧪 Finds contradictions, gaps, or key trends using clustering and embeddings."
    },
    "IdeaGeneratorAgent": {
        "endpoint": "/idea",
        "desc": "💡 Suggests novel research ideas based on literature insights."
    },
}

with st.sidebar:
    st.header("⚙️ Settings")
    backend_url = st.text_input("Backend URL", "http://localhost:8000")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<small>Made with ❤️ for researchers</small>", unsafe_allow_html=True)

add_vertical_space(1)

agent = st.selectbox(
    "Choose an agent",
    list(AGENTS.keys()),
    format_func=lambda x: f"{x} {AGENTS[x]['desc'].split()[0]}"
)

st.markdown(f"<div class='agent-desc'>{AGENTS[agent]['desc']}</div>", unsafe_allow_html=True)

query = st.text_area("Enter your research query or text", height=120)

run = st.button("✨ Run Agent", use_container_width=True)

result = None
if run:
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        endpoint = backend_url + AGENTS[agent]["endpoint"]
        with st.spinner(f"Running {agent}..."):
            try:
                resp = requests.post(endpoint, json={"query": query, "options": {}})
                if resp.ok:
                    result = resp.json().get("result", "No result returned.")
                else:
                    result = f"Error: {resp.status_code} {resp.text}"
            except Exception as e:
                result = f"Request failed: {e}"

if result:
    st.markdown(f"<div class='result-panel'>{result}</div>", unsafe_allow_html=True) 