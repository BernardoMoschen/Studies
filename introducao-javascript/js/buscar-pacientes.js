let botaoAdicionar = document.querySelector("#buscar-pacientes")

botaoAdicionar.addEventListener("click", () => {
    let xhr = new XMLHttpRequest ()
    xhr.open("GET", "https://api-pacientes.herokuapp.com/pacientes")

    xhr.addEventListener("load", () => {
        let resposta = JSON.parse(xhr.responseText) 
    })
    xhr.send()
})