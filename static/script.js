async function sendMessage() {
  const input = document.getElementById("userInput");
  const msg = input.value;
  if (!msg.trim()) return;

  appendToChat("You", msg);
  input.value = "";

  try {
    const res = await fetch("/chatbot", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });
    const data = await res.json();
    appendToChat("CyberBot", data.reply);
  } catch (error) {
    appendToChat("CyberBot", "Oops, something went wrong.");
  }
}

function appendToChat(sender, message) {
  const log = document.getElementById("chatlog");
  const entry = document.createElement("div");
  entry.innerHTML = `<strong>${sender}:</strong> ${message}`;
  log.appendChild(entry);
}
