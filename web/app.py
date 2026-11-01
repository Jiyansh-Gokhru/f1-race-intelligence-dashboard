from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    """Renders the Formula 1 Race Intelligence Dashboard & 9-Scene Story web app."""
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok", "dataset_rows": 13748, "sheets": 5, "visualizations": 9, "story_scenes": 9}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
