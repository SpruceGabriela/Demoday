let janelinhaLateral = document.querySelector('#contato');
let menuHamburguer = document.querySelector('#menuHamburguer')

function abrirMenu(){
    janelinhaLateral.classList.toggle('abrirMenu');
    menuHamburguer.classList.toggle('abrirMenu');
}

menuHamburguer.onclick = abrirMenu