function sendSkill(skill) {
    document.getElementById("user-input").value = skill;
    sendMessage();
}

function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();
    let chatBox = document.getElementById("chat-box");

    if (message === "") return;

    let userDiv = document.createElement("div");
    userDiv.className = "user";
    userDiv.textContent = message;
    chatBox.appendChild(userDiv);

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    let typingDiv = document.createElement("div");
    typingDiv.className = "bot";
    typingDiv.textContent = "Typing...";
    chatBox.appendChild(typingDiv);

    fetch("/get", {
        method: "POST",
        body: JSON.stringify({ msg: message }),
        headers: { "Content-Type": "application/json" }
    })
    .then(res => res.json())
    .then(data => {
        typingDiv.remove();
        let botDiv = document.createElement("div");
        botDiv.className = "bot";
        botDiv.innerHTML = data.response.replace(/\n/g, "<br>");
        chatBox.appendChild(botDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}