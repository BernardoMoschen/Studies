export class Conta {
    #cliente;
    #agencia;
    #saldo;
    static numeroDeContas = 0;

    constructor(cliente, agencia, saldo) {
        if (this.constructor == Conta) {
            throw new TypeError("Você não pode instanciar uma classe abstrata!");
        }
        this.#cliente = cliente;
        this.#agencia = agencia;
        if(saldo){
            this.#saldo = saldo;
        } else {
            this.#saldo = 0;
        }
        Conta.numeroDeContas += 1;
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

   
    sacar(valor, taxa) {
        if (this.caller == Conta) {
            throw new Error("O método sacar da conta é abstrato!")
        }
     }
 
     sacar(valor, taxa){
         const valorSacado = taxa * valor;
         if (this.#saldo >= valorSacado) {
             this.#saldo -= valorSacado.toFixed(2);
             return valorSacado;
         }
 
         return 0;
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
