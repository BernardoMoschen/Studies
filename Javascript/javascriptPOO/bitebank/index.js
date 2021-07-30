import { Cliente } from "./Clientes/Cliente.js";
import { ContaCorrente } from "./Contas/ContaCorrente.js";
import { ContaPoupanca } from "./Contas/ContaPoupanca.js";

const cliente1 = new Cliente('Bernardo', 11223344556);
const cliente2 = new Cliente('Marcelo', 665544332211);

const cC1 = new ContaCorrente(cliente1, 1001);
cC1.depositar(700);
cC1.sacar(400, 1.1);

const cP1 = new ContaPoupanca(cliente2, 2525, 700);
cP1.sacar(400);

cC1.exibeDados();
cP1.exibeDados();

