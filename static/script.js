function flip() {
    const button = document.querySelector('.button');
    button.classList.add('flipping');
    fetch( "/flip", {
        method: "GET"
    }).then(() => {
        button.classList.remove('flipping');
    });
}
