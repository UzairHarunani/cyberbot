import openai
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Insert your new API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful Cyberbullying Awareness Bot for children."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    
    except Exception as e:
        return jsonify({"reply": "Sorry, I am having trouble answering right now."})

if __name__ == "__main__":
    app.run(debug=True)
