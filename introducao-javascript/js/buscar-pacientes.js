let botaoAdicionarPacienteExterno = document.querySelector("#buscar-pacientes")

botaoAdicionarPacienteExterno.addEventListener("click", () => {
    let xhr = new XMLHttpRequest ()
    xhr.open("GET", "https://api-pacientes.herokuapp.com/pacientes")

    xhr.addEventListener("load", () => {
        let pacientes = JSON.parse(xhr.responseText) 

        pacientes.forEach((paciente) => {
            adicionaPacienteNaTabela(paciente)
        })

    })
    xhr.send()
})