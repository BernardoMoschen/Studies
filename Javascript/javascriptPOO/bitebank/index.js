import { Cliente } from "./Cliente.js";
import { contaCorrente } from "./ContaCorrente.js";


const cliente1 = new Cliente();
cliente1.nome = "Bernardo";
cliente1.cpf = 11223344556;
console.log(cliente1);

const cC1 = new contaCorrente;
cC1.agencia = 1001;
cC1.cliente = cliente1;
cC1.depositar(100);
console.log(cC1);


const cliente2 = new Cliente();
cliente2.nome = 'Marcelo';
cliente2.cpf = 65544332211;
console.log(cliente2);

const cC2 = new contaCorrente;
cC2.agencia = 1001;
cC2.cliente = cliente2;
cC2.depositar(500);
console.log(cC2);

cC2.transferir(200, cC1);

cC1.exibeSaldo();
cC2.exibeSaldo();