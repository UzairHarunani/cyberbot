from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Insert your new API key here
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")
    
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # <-- VERY important!!
            messages=[
                {"role": "system", "content": "You are a friendly Cyberbullying Awareness Bot for kids."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = completion.choices[0].message["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error from OpenAI: {e}")
        return jsonify({"reply": "Sorry, I am having trouble answering right now."})

if __name__ == "__main__":
    app.run(debug=True)
