export class SistemaAutenticacao {
    static login(autenticavel, senha) {
        if(SistemaAutenticacao.temAutentificacao(autenticavel)) {
            return autenticavel.autenticar(senha);
        }
        return false
    };

    static temAutentificacao(autenticavel) {
        return "autenticar" in autenticar && autenticavel.autenticar instanceof Function;
    }
}