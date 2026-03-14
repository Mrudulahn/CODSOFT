Rule-Based Chatbot Web Application 🤖
📌 Project Overview

This project is a Rule-Based Chatbot Web Application developed using Python Flask, HTML, CSS, and JavaScript.
The chatbot interacts with users through a simple web interface and responds based on predefined rules.

The goal of this project is to demonstrate basic chatbot development and full-stack communication between frontend and backend.

🚀 Features

Simple and interactive chatbot interface

Real-time communication between frontend and backend

Rule-based response system

Displays current system time

Handles unknown queries with a default response

Lightweight and beginner-friendly implementation

🛠 Technologies Used
Technology	Purpose
Python	Backend programming
Flask	Web framework
HTML	Structure of the chatbot interface
CSS	Styling the chatbot interface
JavaScript	Handling user input and API communication
Fetch API	Sending requests to backend
📂 Project Structure
rule_based_chatbot/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
Description of Files

app.py

Main backend file

Contains chatbot logic and Flask routes

index.html

User interface for the chatbot

Allows users to type and send messages

script.js

Handles sending messages to the Flask server

Displays responses from the chatbot

style.css

Styles the chatbox and interface

⚙️ How It Works

The user types a message in the chat input box.

JavaScript sends the message to the Flask server using Fetch API.

Flask receives the message through the /chat API endpoint.

The message is processed by the chatbot_response() function.

The chatbot returns an appropriate response.

The response is displayed in the chat interface.

💬 Example Conversations
User Message	Bot Response
Hello	Hello! How can I help you?
What is your name?	I am a rule-based chatbot.
What is the time?	Current time is HH
Bye	Goodbye! Have a great day.
Random message	Sorry, I didn't understand that.
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/rule-based-chatbot.git
2️⃣ Navigate to Project Folder
cd rule-based-chatbot
3️⃣ Install Flask
pip install flask
4️⃣ Run the Application
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000

Learning Outcomes

Through this project, I was able to learn:

Building a Flask web application

Creating REST API endpoints

Frontend and backend communication

Using JavaScript Fetch API

Implementing a rule-based chatbot system