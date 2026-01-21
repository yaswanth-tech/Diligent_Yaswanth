function send() {
  const msgInput = document.getElementById("msg");
  const chat = document.getElementById("chat");
  const msg = msgInput.value.trim();
  if (!msg) return;

  chat.innerHTML += `<p><b>You:</b> ${msg}</p>`;
  msgInput.value = "";

  fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: msg})
  })
    .then(res => res.json())
    .then(data => {
      const sources = (data.sources || [])
        .map(s => s.text)
        .filter(Boolean)
        .join(" | ");
      chat.innerHTML += `<p><b>Assistant:</b> ${data.reply}</p>`;
      if (sources) {
        chat.innerHTML += `<p class="sources">Context: ${sources}</p>`;
      }
      chat.scrollTop = chat.scrollHeight;
    })
    .catch(() => {
      chat.innerHTML += `<p class="error">Something went wrong.</p>`;
    });
}
