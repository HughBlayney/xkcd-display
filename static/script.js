function flip() {
    const button = document.querySelector('#flip_button');
    button.classList.add('flipping');
    fetch( "/flip", {
        method: "GET"
    }).then(() => {
        button.classList.remove('flipping');
    });
}

function random() {
    const button = document.querySelector('#random_button');
    button.classList.add('flipping');
    fetch( "/random", {
        method: "GET"
    }).then(() => {
        button.classList.remove('flipping');
    });
}

