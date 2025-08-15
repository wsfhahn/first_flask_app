import wikipedia
from flask import Blueprint, request, jsonify

search_bp = Blueprint("search", __name__, url_prefix="/api")

@search_bp.post("/search")
def search(): # type: ignore
    term = (request.json or {}).get("term", "").strip()
    if not term:
        return jsonify({"error": "Missing term"})
    try:
        results: list[str] = wikipedia.search(term)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print(wikipedia.search("apple silicon"))