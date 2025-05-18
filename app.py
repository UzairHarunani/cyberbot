from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Insert your new API key directly here
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"reply": "Please ask something about cyberbullying."})

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly Cyberbullying Awareness Bot for children."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.5,  # Optional: control creativity
            max_tokens=150    # Optional: control answer length
        )
        reply = completion.choices[0].message["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error from OpenAI: {e}")  # IMPORTANT: show full error in logs
        return jsonify({"reply": "Sorry, I am having trouble answering right now."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
