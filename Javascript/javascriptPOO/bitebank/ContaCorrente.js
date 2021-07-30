export class contaCorrente {
    #saldo;
    agencia;
    #cliente;

    constructor(){
        this.#saldo = 0;
        this.agencia = undefined;
        this.#cliente = undefined;
    }

    set cliente(novoCliente) {
        if (novoCliente instanceof Cliente) {
            this.#cliente = novoCliente;
        } 
        else {
            console.log('Atribuição inválida.');
        }
    }

    get cliente() {
        return this.#cliente;
    }

    get saldo() {
        return this.#saldo;
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

    transferir(valor, conta) {
        const valorSacado = this.sacar(valor);
        conta.depositar(valorSacado);
    }
}