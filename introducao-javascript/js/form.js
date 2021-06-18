
// Função de adicionar pacientes na tabela, via formulário
var botaoAdicionar = document.querySelector("#adicionar-paciente")
botaoAdicionar.addEventListener("click", (event) => {
    event.preventDefault()
    let form = document.querySelector("#form-adiciona")

// Extrai informações do paciente do form
    var paciente = obtemPacienteDoFormulario(form)

// Cria a Tr e a Td do paciente
    montaTr(paciente)

// Adiciona o paciente na tabela
    var tabela = document.querySelector("#tabela-pacientes")

    tabela.appendChild(pacienteTr)
})

// Função p/ obter dados do paciente obtidos pelo formulário
var  obtemPacienteDoFormulario = (form) => {

    var paciente = {
        nome: form.name.value,
        peso: form.name.value,
        altura: form.name.value,
        gordura: form.name.value,
        imc: calculaImc(form.peso.value, form.altura.value)
    }

    return pacientes
}

// Função p/ montar uma Tr com os dados do paciente
var montaTr = (paciente) => {

    var pacienteTr = document.createElement("tr")
    pacienteTr.classList.add("paciente")

    var nomeTd = montaTd(paciente.nome, "info-nome")
    var pesoTd = montaTd(paciente.peso, "info-peso")
    var alturaTd = montaTd(paciente.altura, "info-altura")
    var gorduraTd = montaTd(paciente.gordura, "info-gordura")
    var imcTd = montaTd(paciente.imc, "info-imc")

    pacienteTr.appendChild(pesoTd)
    pacienteTr.appendChild(alturaTd)
    pacienteTr.appendChild(nomeTd)
    pacienteTr.appendChild(gorduraTd)
    pacienteTr.appendChild(imcTd)

}

// Função p/ montar uma Td com os dados do paciente
var montaTd = (dado, classe) => {

    var td = document.createElement("td")
    td.textContent = dado
    td.classList.add(classe)
    return td
}