let tabela = document.querySelector("#tabela-pacientes")
tabela.addEventListener("dblclick", () => {
    if (event.target.tagName == 'TD') {
        event.target.parentNode.remove()
    }
})