export class Conta {
    #cliente;
    #agencia;
    #saldo;

    constructor(cliente, agencia, saldo) {
        this.#cliente = cliente;
        this.#agencia = agencia;
        this.#saldo = saldo;
    }

    set cliente(novoCliente) {
        if (novoCliente instanceof Cliente) {
            this.#cliente = novoCliente;
        }
    }

    set saldo(valor) {
        this.#saldo = valor;
    }

    get cliente() {
        return this.#cliente;
    }

    get agencia() {
        return this.#agencia;
    }

    get saldo() {
        return this.#saldo;
    }

   
    sacar(valor){
        if(Number.parseFloat(valor) && this.#saldo >= valor) {
            this.#saldo -= valor;
        }
    }

    depositar(valor){
        if(Number.parseFloat(valor) && this.#saldo >= 0) {
            this.saldo += valor;
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