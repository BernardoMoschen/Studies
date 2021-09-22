import { Conta } from "./Conta.js";

export class ContaPoupanca extends Conta{
#sacar
    constructor(cliente, agencia, saldo) {
        super(cliente, agencia, saldo);
    }

    sacar(valor){
        const taxa = 1.02;
        return super.sacar(valor, taxa);
    }
}