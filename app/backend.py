"""
Backend logic for agent orchestration and API endpoints.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.api_clients import search_semantic_scholar, cohere_summarize, extract_citations_regex, cluster_abstracts, cohere_idea_generator

app = FastAPI()

# Allow CORS for local Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str
    options: dict = {}

@app.post("/literature")
def literature_agent(req: QueryRequest):
    results = search_semantic_scholar(req.query)
    if results and "error" in results[0]:
        return {"result": f"Error: {results[0]['error']}"}
    if not results:
        return {"result": "No papers found."}
    out = []
    for i, paper in enumerate(results, 1):
        abstract = paper['abstract'] or ''
        out.append(f"<b>{i}. <a href='{paper['url']}' target='_blank'>{paper['title']}</a></b> ({paper['year']})<br>"
                   f"<i>{paper['authors']}</i><br>"
                   f"<small>{abstract[:300]}{'...' if len(abstract) > 300 else ''}</small><br><br>")
    return {"result": "".join(out)}

@app.post("/summarize")
def summarizer_agent(req: QueryRequest):
    result = cohere_summarize(req.query)
    if 'error' in result:
        return {"result": f"Error: {result['error']}"}
    return {"result": result['summary']}

@app.post("/citation")
def citation_agent(req: QueryRequest):
    citations = extract_citations_regex(req.query)
    if not citations:
        return {"result": "No citations found."}
    out = [f"<li>{c}</li>" for c in citations]
    return {"result": f"<ul>{''.join(out)}</ul>"}

@app.post("/insight")
def insight_agent(req: QueryRequest):
    abstracts = req.options.get('abstracts') if req.options and 'abstracts' in req.options else [req.query]
    clusters = cluster_abstracts(abstracts)
    if 'error' in clusters:
        return {"result": f"Error: {clusters['error']}"}
    out = []
    for label, texts in clusters.items():
        out.append(f"<b>Cluster {label+1} ({len(texts)} papers):</b><br>" + '<br>'.join(f"- {t[:120]}{'...' if len(t)>120 else ''}" for t in texts) + "<br><br>")
    return {"result": "".join(out)}

@app.post("/idea")
def idea_generator_agent(req: QueryRequest):
    result = cohere_idea_generator(req.query)
    if 'error' in result:
        return {"result": f"Error: {result['error']}"}
    out = [f"<li>{idea}</li>" for idea in result['ideas']]
    return {"result": f"<ul>{''.join(out)}</ul>"} 