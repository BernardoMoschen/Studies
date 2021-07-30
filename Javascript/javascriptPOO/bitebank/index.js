import { Cliente } from "./Cliente.js";
import { contaCorrente } from "./ContaCorrente.js";


const cliente1 = new Cliente();
cliente1.nome = "Bernardo";
cliente1.cpf = 11223344556;
console.log(cliente1);

const contaCorrenteBernardo = new contaCorrente;
contaCorrenteBernardo.agencia = 1001;
contaCorrenteBernardo.cliente = cliente1;
contaCorrenteBernardo.depositar(100);
console.log(contaCorrenteBernardo);

const cliente2 = new Cliente();
cliente2.nome = 'Marcelo';
cliente2.cpf = 65544332211
console.log(cliente2);

const contaCorrenteMarcelo = new contaCorrente;
contaCorrenteMarcelo.agencia = 1001
contaCorrenteMarcelo.cliente = cliente2;
contaCorrenteMarcelo.depositar(500);
console.log(contaCorrenteMarcelo)