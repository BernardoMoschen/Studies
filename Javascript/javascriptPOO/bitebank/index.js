// import { Cliente } from "./Clientes/Cliente.js";
import { Gerente } from "./Funcionários/Gerente.js";
import { Diretor } from "./Funcionários/Diretor.js";
import { SistemaAutenticacao } from "./Autenticacao/Login.js";


const diretor1 = new Diretor("Rodrigo", 1000, 778899112233)
diretor1.cadastrarSenha(112255)

const geretir1 = new Gerente("Alberto", 500, 112233445566)
diretor1.cadastrarSenha(661122)

const isLogado = SistemaAutenticacao.login(diretor1, 112255)

console.log(isLogado)

// import { Conta } from "./Contas/Conta.js";
// import { ContaCorrente } from "./Contas/ContaCorrente.js";
// import { ContaPoupanca } from "./Contas/ContaPoupanca.js";

// const cliente1 = new Cliente('Bernardo', 11223344556);
// const cliente2 = new Cliente('Marcelo', 665544332211);

// const cC1 = new ContaCorrente(cliente1, 1001);
// cC1.depositar(700);
// cC1.sacar(400);

// const cP1 = new ContaPoupanca(cliente2, 2525, 700);
// cP1.sacar(400);

// cC1.exibeDados();
// cP1.exibeDados();


// console.log(Conta.numeroDeContas)
