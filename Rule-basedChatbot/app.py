from flask import Flask, render_template, request, jsonify
from datetime import datetime
app = Flask(__name__)

def chatbot_response(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "name" in message:
        return "I am a rule-based chatbot."

    elif "time" in message:
        now = datetime.now().strftime("%H:%M")
        return "Current time is " + now

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I didn't understand that."
    
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    bot_reply = chatbot_response(user_message)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)


