document.getElementById("checkBtn").addEventListener("click", () => {
    const password = document.getElementById("passwordInput").value;
    
    fetch("/check", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({password: password})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("verdict").innerText = data.verdict;
        document.getElementById("score").innerText = data.score;
        const list = document.getElementById("suggestions");
        list.innerHTML = "";
        data.suggestions.forEach(item => {
            const li = document.createElement("li");
            li.innerText = item;
            list.appendChild(li);
        });
    });
});
