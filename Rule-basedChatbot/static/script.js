function sendMessage(){

    let input = document.getElementById("userInput");
    let message = input.value;

    if(message.trim() === ""){
        return;
    }

    let chatbox = document.getElementById("chatbox");

    // Show user message
    let userMsg = document.createElement("p");
    userMsg.textContent = "You: " + message;
    chatbox.appendChild(userMsg);

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {

        // Show bot reply
        let botMsg = document.createElement("p");
        botMsg.textContent = "Bot: " + data.reply;
        chatbox.appendChild(botMsg);

    });

    input.value = "";
}