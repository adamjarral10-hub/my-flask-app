from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/greet", methods=["POST"])
def greet():
    """Returns a personalised greeting (used by the contact form demo)."""
    data = request.get_json(silent=True) or {}
    name = data.get("name", "").strip() or "Stranger"
    now  = datetime.now().strftime("%H:%M on %d %B %Y")
    return jsonify({
        "message": f"Hello, {name}! 👋  You reached the server at {now}.",
        "status":  "ok"
    })


@app.route("/api/ping")
def ping():
    """Health-check endpoint — useful for deployment platforms."""
    return jsonify({"status": "ok", "time": datetime.utcnow().isoformat() + "Z"})


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Use host="0.0.0.0" so it's reachable inside Docker / cloud containers.
    # Debug mode is fine locally; it is disabled automatically by gunicorn in prod.
    app.run(host="0.0.0.0", port=5000, debug=True)
