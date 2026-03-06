function updateClock() {
    const ora = new Date().toLocaleTimeString('it-IT', { hour12: false });
    const el = document.getElementById("clock") || document.querySelector(".clock");
    if(el) el.innerText = ora;
}

function updateData() {
    fetch("market_status.json?t=" + new Date().getTime())
    .then(r => r.json())
    .then(data => {
        if(document.getElementById("btc-price")) document.getElementById("btc-price").innerText = data.price || "$ --,---.--";
        if(document.getElementById("status-text")) document.getElementById("status-text").innerText = data.status || "OFFLINE";
        if(document.getElementById("signal-text")) document.getElementById("signal-text").innerText = data.signal || "ANALYZING";
    })
    .catch(e => console.log("Errore dati"));
}

setInterval(updateClock, 1000);
setInterval(updateData, 5000);
updateClock();
updateData();
