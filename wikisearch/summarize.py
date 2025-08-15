from openai import OpenAI
import wikipedia
from flask import Blueprint, jsonify, request
from os import getenv
from dotenv import load_dotenv

from wikisearch.inference import get_model_response, Config
from wikisearch.prompts import summarizer_system_prompt, summarizer_user_prompt

load_dotenv()
BASE_URL = getenv("BASE_URL")
API_KEY = getenv("API_KEY")
MODEL_ID = getenv("MODEL_ID")

if not BASE_URL:
    raise ValueError("BASE_URL cannot be empty. Please set the BASE_URL variable in your env.")
if not API_KEY:
    raise ValueError("API_KEY cannot be empty. Please set the API_KEY variable in your env.")
if not MODEL_ID:
    raise ValueError("MODEL_ID cannot by empty. Please set the MODEL_ID variable in your env.")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

config = Config(
    model=MODEL_ID,
    temperature=0.7,
    top_p=0.95
)

summarize_bp = Blueprint("summarize", __name__, url_prefix="/api")

@summarize_bp.post("/summarize")
def summarize(): #type: ignore
    title = (request.json or {}).get("title", "").strip()
    if not title:
        return jsonify({"error": "Missing title"})
    try:
        page = wikipedia.page(title, auto_suggest=False)
        content = page.content[:12000]
        summary = get_model_response(
            summarizer_system_prompt,
            summarizer_user_prompt.format(title=title, content=content),
            client=client,
            config=config
        )

        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": f"Failed to get summary from model: {str(e)}"})
