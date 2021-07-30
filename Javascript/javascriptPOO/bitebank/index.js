import { Cliente } from "./Cliente.js";
import { ContaCorrente } from "./ContaCorrente.js";


const cliente1 = new Cliente('Bernardo', 11223344556);
console.log(cliente1);

const cliente2 = new Cliente('Marcelo', 65544332211);
console.log(cliente2);

const cC1 = new ContaCorrente(1001, cliente1);
cC1.depositar(100);

const cC2 = new ContaCorrente(1001, 'Alberto');
cC2.depositar(500);
cC2.transferir(200, cC1);


