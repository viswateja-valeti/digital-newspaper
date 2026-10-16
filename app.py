
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Digital Newspaper Subscription System"

@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json(silent=True) or {}
    if not data.get("name") or not data.get("plan"):
        return jsonify({"error": "Name and plan are required"}), 400

    return jsonify({
        "message": "Subscription successful",
        "name": data["name"],
        "plan": data["plan"]
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
