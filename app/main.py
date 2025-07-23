from flask import Flask, request, jsonify, redirect
from app.shortener import generate_short_code, is_valid_url
from app.storage import URLStore

app = Flask(__name__)
store = URLStore()

@app.route("/api/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    url = data["url"]
    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    while store.get(short_code):
        short_code = generate_short_code()

    store.add(short_code, url)
    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@app.route("/<short_code>", methods=["GET"])
def redirect_short_url(short_code):
    record = store.get(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404

    store.increment_click(short_code)
    return redirect(record["url"])

@app.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    record = store.stats(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": record["url"],
        "clicks": record["clicks"],
        "created_at": record["created_at"].isoformat()
    })
