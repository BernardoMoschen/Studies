import { Conta } from "./Conta.js";

export class ContaSalario extends Conta{
#sacar
    constructor(cliente, agencia){
        super(cliente, agencia, 0);
    }

    sacar(valor){
        const taxa = 1.01;
        return super.sacar(valor, taxa);
    }
}