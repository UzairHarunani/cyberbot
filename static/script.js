async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value;
  if (!message.trim()) return;

  appendToChat("You", message);
  input.value = "";

  const res = await fetch("/chatbot", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  });

  const data = await res.json();
  appendToChat("CyberBot", data.response);
}

function appendToChat(sender, text) {
  const log = document.getElementById("chatlog");
  const msg = document.createElement("p");
  msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
  log.appendChild(msg);
  log.scrollTop = log.scrollHeight;
}
