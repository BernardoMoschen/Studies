import { Cliente } from "./Cliente.js";

export class ContaCorrente {
    #saldo;
    agencia;
    #cliente;

    set cliente(novoCliente) {
        if (novoCliente instanceof Cliente) {
            this.#cliente = novoCliente;
        }
    }

    get cliente() {
        return this.#cliente;
    }

    get saldo() {
        return this.#saldo;
    }

    constructor(agencia, cliente){
        this.#saldo = 0;
        this.agencia = agencia;
        this.#cliente = cliente;
    }

    sacar(valor){
        if(Number.parseFloat(valor) && this.#saldo >= valor) {
            this.#saldo -= valor;
        }
    }

    depositar(valor){
        if(Number.parseFloat(valor) && this.#saldo >= 0) {
            this.#saldo += valor;
        }
    }

    transferir(valor, conta) {
        const valorSacado = this.sacar(valor);
        conta.depositar(valorSacado);
    }
}