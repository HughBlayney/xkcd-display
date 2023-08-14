function flip() {
    const button = document.querySelector('.button');
    button.classList.add('flipping');
    fetch("{{ ngrok_url }}/flip", {
        method: "GET"
    }).then(() => {
        button.classList.remove('flipping');
    });
}
