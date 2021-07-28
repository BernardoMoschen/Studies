class Cliente {
    nome;
    cpf;
    
    constructor(nome, cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }
}

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

const cliente1 = new Cliente();
cliente1.nome = "Bernardo";
cliente1.cpf = 11223344556;

console.log(cliente1)
// const cliente2 = new Cliente();
// cliente2.nome = 'Marcelo';
// cliente2.cpf = 65544332211;

const contaCorrenteBernardo = new contaCorrente;
contaCorrenteBernardo.agencia = 1001;

// const contaCorrenteMarcelo = new contaCorrente;
// contaCorrenteBernardo.agencia = 1001;

contaCorrenteBernardo.depositar(100);
console.log(contaCorrenteBernardo);
