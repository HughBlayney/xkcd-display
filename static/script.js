function flip() {
    const button = document.querySelector('.button');
    button.classList.add('flipping');
    fetch(NGROK_URL + "/flip", {
        method: "GET"
    }).then(() => {
        button.classList.remove('flipping');
    });
}
