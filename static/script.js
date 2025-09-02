document.getElementById("suggestBtn").onclick = async () => {
    let prompt = document.getElementById("prompt").value;
    let res = await fetch("/suggest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });
    let data = await res.json();
    document.getElementById("suggestion").innerText = data.suggestion || data.error;
};

document.getElementById("buyCreditsBtn").onclick = async () => {
    let res = await fetch("/create-payment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ amount: 100, email: "test@example.com" })
    });
    let data = await res.json();
    if (data.payment_link) {
        window.location.href = data.payment_link;
    } else {
        alert("Error: " + data.error);
    }
};
