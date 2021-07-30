import { Cliente } from "./Cliente.js";
import { ContaCorrente } from "./ContaCorrente.js";
import { ContaPoupanca } from "./ContaPoupanca.js";

const cliente1 = new Cliente('Bernardo', 11223344556);
const cliente2 = new Cliente('Marcelo', 665544332211);

const cC1 = new ContaCorrente(cliente1, 1001);
cC1.depositar(700);
cC1.sacar(400);

const cP1 = new ContaPoupanca(cliente2, 2525, 500);

cC1.exibeDados();
cP1.exibeDados();

