import { Cliente } from "./Cliente.js";
import { ContaCorrente } from "./ContaCorrente.js";
import { ContaPoupanca } from "./ContaPoupanca.js";
import { Conta } from "./Conta.js";


const cliente1 = new Cliente('Bernardo', 11223344556);

const cC1 = new Conta(0, cliente1, 1001);
cC1.depositar(700);
cC1.sacar(200);

const cP1 = new Conta(50, cliente1, 1001);

cC1.exibeDados();


