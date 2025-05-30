# app.py
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all cross-origin requests (for frontend)

OPENROUTER_API_KEY = "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"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    result = response.json()

    try:
        reply = result["choices"][0]["message"]["content"]
    except Exception as e:
        reply = "Sorry, an error occurred."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
