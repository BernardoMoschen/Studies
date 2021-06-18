let titulo = document.querySelector(".titulo")
titulo.textContent = "Bernardo"
titulo.textContent += ' Nutricionista'

var pacientes = document.querySelectorAll(".paciente");

for (let pacientee of pacientes) {
// Definindo o paciente como o id que representa o primeiro paciente. 
let paciente = pacientee

// Definindo o nome do paciente conforme a classe que representa o nome da variável paciente(conforme o DOM)
let nomePaciente = paciente.querySelector(".info-nome")

// Definindo o peso do paciente conforme a classe que representa o peso da variável paciente(conforme o DOM)
let pesoPaciente = paciente.querySelector(".info-peso")

// Definindo a altura do paciente conforme a classe que representa o altura da variável paciente(conforme o DOM)
let alturaPaciente = paciente.querySelector(".info-altura")

// Capturando o valor do IMC do paciente presente no DOM
var imcAttPaciente = paciente.querySelector(".info-imc")

// Criando variáveis para armazenar o valor em texto
var nome = nomePaciente.textContent
var peso = pesoPaciente.textContent
var altura = alturaPaciente.textContent
var imc = imcAttPaciente.textContent

// Definindo valores booleanos para validação de peso e altura
let alturaValida = true 
let pesoValido = true

// Validação das medidas do paciente
if (peso <= 0 || peso >= 1000) {
    console.log("Peso inválido!");
    pesoPaciente.textContent = "Peso inválido!";
    pesoValido = false;
    paciente.classList.add("paciente-invalido")
}

if (altura <= 0 || altura >= 3) {
    console.log("Altura inválida!");
    alturaPaciente.textContent = "Altura inválida!";
    alturaValida = false;
    paciente.classList.add("paciente-invalido")
}

// Cálculo do IMC
imcAttPaciente.textContent = "Altura e/ou peso inválidos!"
if (alturaValida && pesoValido) {
    imc = peso / (altura * altura);
    imcAttPaciente.textContent = imc.toFixed(2);    
}
}
// Console.log de saída
console.log(`O paciente: ${nome}, tem o peso: ${peso}, a altura: ${altura} e o IMC: ${imcAttPaciente.textContent}.`)    