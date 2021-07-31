export class Cliente {
    #cpf;
    #senha

    get cpf() {
        return this.#cpf;
    }

    constructor(nome, cpf) {
        this.nome = nome;
        this.#cpf = cpf;
        this.#senha = null;
    }   

    autenticar(senha) {
        return senha == this.#senha; 
    }

    cadastrarSenha(senha){
        this.#senha = senha;
    }
}