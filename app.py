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
