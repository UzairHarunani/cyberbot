from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# 🔐 Insert your OpenAI key here
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message", "")
    print("[USER INPUT]", user_message)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are CyberBot, a kind and helpful chatbot that teaches children about cyberbullying in a friendly way."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.5,
        )

        reply = response['choices'][0]['message']['content']
        print("[CYBERBOT REPLY]", reply)

        return jsonify({"response": reply})

    except Exception as e:
        print("[ERROR]", str(e))
        return jsonify({"response": "Sorry, I'm having trouble answering right now. Please try again later."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
