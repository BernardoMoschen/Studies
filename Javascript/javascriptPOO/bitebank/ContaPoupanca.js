import { Conta } from "./Conta.js";

export class ContaPoupanca extends Conta{

    constructor(cliente, agencia, saldo) {
        super(cliente, agencia, saldo);
    }
}