const apiUrl = "http://127.0.0.1:8000/test/";

function addNewQuestion() {
    let prompt = window.prompt("Quelle est ta question?")
    let chatBoxEl = document.getElementById("chat-add");
    let msgEl = document.createElement("p");
    msgEl.innerText = prompt;
    msgEl.classList.add("chat-msg");
    msgEl.classList.add("chat-question");
    chatBoxEl.appendChild(msgEl);
    let reponseEl = document.createElement("p");
    chatBoxEl.appendChild(reponseEl);
    reponseEl.classList.add("chat-msg");
    reponseEl.classList.add("chat-reponse");
    reponseEl.innerText = "...";
    
    fetch('http://127.0.0.1:8000/chat/?prompt=' + prompt, {method: "POST"})
    .then(response => {
      return response.json();
    })
    .then(data => {
      reponseEl.innerText = data;
    })
}

