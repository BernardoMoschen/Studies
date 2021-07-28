class Cliente {
    nome;
    cpf;
}

class contaCorrente {
    saldo;
    agencia;

    sacar(valor){
        if(this.saldo >= valor) {
            this.saldo -= valor;
        }
    }   
}

const cliente1 = new Cliente();
const cliente2 = new Cliente();
const cliente3 = new Cliente();

cliente1.nome = 'Bernardo';
cliente1.cpf = 11223344556;

cliente2.nome = 'Marcelo';
cliente2.cpf = 65544332211;

const contaCorrenteBernardo = new contaCorrente;
contaCorrenteBernardo.agencia = 1001;
contaCorrenteBernardo.saldo = 0;



const contaCorrenteMarcelo = new contaCorrente;
contaCorrenteBernardo.agencia = 1001;
contaCorrenteBernardo.saldo = 0;

