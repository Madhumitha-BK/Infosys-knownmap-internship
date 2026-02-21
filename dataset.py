from fastapi import APIRouter
from pydantic import BaseModel
import wikipedia
import requests

router = APIRouter(prefix="/dataset", tags=["Dataset"])

# -------- Request Model --------
class DatasetRequest(BaseModel):
    sources: list[str]
    topic: str

# -------- Wikipedia Fetch --------
def fetch_wikipedia(topic: str):
    wikipedia.set_lang("en")
    return wikipedia.summary(topic, sentences=5)

# -------- ArXiv Fetch --------
def fetch_arxiv(topic: str):
    url = f"http://export.arxiv.org/api/query?search_query=all:{topic}&max_results=3"
    response = requests.get(url)
    return response.text

# -------- Unified Loader --------
@router.post("/load")
def load_dataset(request: DatasetRequest):
    data = {}

    if "wikipedia" in request.sources:
        data["wikipedia"] = fetch_wikipedia(request.topic)

    if "arxiv" in request.sources:
        data["arxiv"] = fetch_arxiv(request.topic)

    return data
