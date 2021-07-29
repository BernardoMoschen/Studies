class contaCorrente {
    #saldo;

    constructor(agencia){
        this.#saldo = 0
        this.agencia = agencia;
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