
// Função de adicionar pacientes na tabela, via formulário
var botaoAdicionar = document.querySelector("#adicionar-paciente")
botaoAdicionar.addEventListener("click", (event) => {
    event.preventDefault()

    let form = document.querySelector("#form-adiciona")

// Extrai informações do paciente do form
    var paciente = obtemPacienteDoFormulario(form)

// Verifica se existe erros nos dados do paciente
    var erros = validaPaciente(pacientes)
    if (erros.length > 0) {
        exibeMensagensErro(erros)
        return
    }

    adicionaPacienteNaTabela(paciente)
    form.reset()
    
// Remove as mensagens de erro, caso seja inserido um paciente válido
var mensagensErro = document.querySelector("#mensagens-erro");
mensagensErro.innerHTML = "";
})

// Função p/ obter dados do paciente obtidos pelo formulário
var obtemPacienteDoFormulario= (form) => {

    var paciente = {
        nome: form.nome.value,
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value,
        imc: calculaImc(form.peso.value, form.altura.value)
    }
    return paciente
}
// Função p/ montar uma Tr com os dados do paciente
var montaTr = (paciente) => {

    var pacienteTr = document.createElement("tr")
    pacienteTr.classList.add("paciente")

    pacienteTr.appendChild(montaTd(paciente.nome, "info-nome"))
    pacienteTr.appendChild(montaTd(paciente.peso, "info-peso"))
    pacienteTr.appendChild(montaTd(paciente.altura, "info-altura"))
    pacienteTr.appendChild(montaTd(paciente.gordura, "info-gordura"))
    pacienteTr.appendChild(montaTd(paciente.imc, "info-imc"))

    return pacienteTr
}

// Função p/ montar uma Td com os dados do paciente
var montaTd = (dado, classe) => {

    var td = document.createElement("td")
    td.textContent = dado
    td.classList.add(classe)
    return td
}

// Função p/ adicionar paciente na tabela
let adicionaPacienteNaTabela = (paciente) => {
// Cria a Tr e a Td do paciente
var pacienteTr = montaTr(paciente)

// Adiciona o paciente na tabela
var tabela = document.querySelector("#tabela-pacientes")
tabela.appendChild(pacienteTr)
}

// Função p/ validar o paciente
let validaPaciente = (paciente) => {
    let erros = []

    if (paciente.nome == null) {
        erros.push("O campo nome é obrigatório!")
    }

    if (paciente.altura == null) {
        erros.push("O campo altura é obrigatório!")
    }

    if (paciente.peso == null) {
        erros.push("O campo peso é obrigatório!")
    }

    if (paciente.gordura == null) {
        erros.push("O campo gordura é obrigatório!")
    }

    if (!validaPeso(paciente.peso)) {
        erros.push("Peso é inválido")
    }

    if (!validaAltura(paciente.altura)) {
        erros.push("Altura é inválida!")
    }

    return erros
}

// Função que exibe mensagens de erro
let exibeMensagensErro = (erros) => {
    var ul = document.querySelector("#mensagens-erro")
    ul.innerHTML = ""

    erros.forEach(erro => {
        var li = document.createElement("li")
        li.textContent = erro
        ul.appendChild(li)
    });
}