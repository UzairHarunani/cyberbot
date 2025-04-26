from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Load API Key
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
                {"role": "system", "content": "You are CyberBot, a friendly chatbot that helps kids understand and deal with cyberbullying."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": "Sorry, I'm having trouble answering right now."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
