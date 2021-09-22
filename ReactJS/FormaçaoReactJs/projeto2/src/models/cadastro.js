function validaCPF(cpf) {
  const cpfValido = /^\d{3}.?\d{3}.?\d{3}-?\d{2}$/;
  if (!cpfValido.test(cpf)) {
    return { valido: false, texto: 'CPF deve estar no formato: XXX.XXX.XXX-XX' };
  }
  return { valido: true, texto: '' };
}

function validaSenha(senha) {
  const senhaValida = /\d{7,}/;
  if (!senhaValida.test(senha)) {
    return { valido: false, texto: 'A senha deve ter no mínimo 7 dígitos.' };
  }
  return { valido: true, texto: '' };
}

function validaNome(nome) {
  const nomeValido = /\w{3,}/;
  if (!nomeValido.test(nome)) {
    return { valido: false, texto: 'O nome deve ter no mínimo 3 dígitos.' };
  }
  return { valido: true, texto: '' };
}

export { validaCPF, validaSenha, validaNome };
