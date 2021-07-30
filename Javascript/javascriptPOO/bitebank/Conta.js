export class Conta {
    #saldo;
    #cliente;
    #agencia;

    constructor(saldoInicial, cliente, agencia) {
        this.#saldo = saldoInicial;
        this.#cliente = cliente;
        this.#agencia = agencia;
    }

    get cliente() {
        return this.#cliente;
    }

    get saldo() {
        return this.#saldo;
    }

    get agencia() {
        return this.#agencia;
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

    exibeDados(){
        console.log("Cliente: " + this.cliente.nome + " Ag: " + this.agencia + " Saldo: " + this.saldo)
    }
}
