export class contaCorrente {
    #saldo;
    agencia;
    cliente;

    constructor(){
        this.#saldo = 0;
    }

    sacar(valor){
        if(this.#saldo >= valor) {
            this.#saldo -= valor;
        }
    }

    depositar(valor){
        if(this.#saldo >= 0) {
            this.#saldo += valor;
        }
    }
}