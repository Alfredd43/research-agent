"""
API clients for Semantic Scholar, arXiv, and GROBID.
"""

import requests
import json
import os
import re
from typing import List

def search_semantic_scholar(query, limit=5):
    """
    Search Semantic Scholar for papers matching the query.
    Returns a list of dicts: title, authors, url, year, abstract.
    """
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,url,year,abstract"
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        results = []
        for paper in data.get("data", []):
            results.append({
                "title": paper.get("title"),
                "authors": ", ".join([a.get("name", "") for a in paper.get("authors", [])]),
                "url": paper.get("url"),
                "year": paper.get("year"),
                "abstract": paper.get("abstract", "")
            })
        return results
    except Exception as e:
        return [{"error": str(e)}]

def get_cohere_api_key():
    try:
        with open(os.path.join(os.path.dirname(__file__), '../config/cohere_keys.json')) as f:
            data = json.load(f)
            return data.get('cohere_api_key')
    except Exception:
        return None

def cohere_summarize(text):
    api_key = get_cohere_api_key()
    if not api_key:
        return {'error': 'Cohere API key not found.'}
    url = 'https://api.cohere.ai/v1/summarize'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'text': text,
        'length': 'medium',
        'format': 'paragraph',
        'model': 'command-r-plus',
        'extractiveness': 'auto'
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return {'summary': data.get('summary', '')}
    except Exception as e:
        return {'error': str(e)}

def extract_citations_regex(text):
    """
    Extracts citation-like patterns from text using regex.
    Returns a list of found citations (strings).
    """
    # Simple regex for [1], (Smith et al., 2020), etc.
    pattern = r"(\[[0-9]+\]|\([A-Z][a-z]+ et al\\.,? \d{4}\))"
    matches = re.findall(pattern, text)
    # Also try to extract reference-like lines (APA/IEEE)
    ref_lines = re.findall(r"^.+\d{4}.+$", text, re.MULTILINE)
    return list(set(matches + ref_lines))

def cluster_abstracts(texts: List[str], n_clusters=2):
    """
    Cluster a list of texts (abstracts) using sentence-transformers and KMeans.
    Returns a dict: {cluster_label: [texts]}
    """
    try:
        from sentence_transformers import SentenceTransformer
        from sklearn.cluster import KMeans
    except ImportError:
        return {"error": "sentence-transformers and scikit-learn required."}
    if not texts:
        return {"error": "No texts provided."}
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    kmeans = KMeans(n_clusters=min(n_clusters, len(texts)), random_state=42)
    labels = kmeans.fit_predict(embeddings)
    clusters = {}
    for label, text in zip(labels, texts):
        clusters.setdefault(label, []).append(text)
    return clusters

def cohere_idea_generator(topic):
    api_key = get_cohere_api_key()
    if not api_key:
        return {'error': 'Cohere API key not found.'}
    url = 'https://api.cohere.ai/v1/generate'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    prompt = f"Suggest 3 novel, creative, and feasible research ideas for the following topic or text.\nTopic: {topic}\nIdeas:"
    payload = {
        'model': 'command-r-plus',
        'prompt': prompt,
        'max_tokens': 200,
        'temperature': 0.8,
        'stop_sequences': ['\n\n']
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        text = data.get('generations', [{}])[0].get('text', '')
        # Split into ideas (numbered or bulleted)
        ideas = [line.strip('- ').strip() for line in text.split('\n') if line.strip()]
        return {'ideas': ideas}
    except Exception as e:
        return {'error': str(e)}

# TODO: Implement API client wrappers 