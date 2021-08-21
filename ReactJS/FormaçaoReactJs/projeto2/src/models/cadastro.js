function validaCPF(cpf) {
  const cpfValido = /^\d{3}.?\d{3}.?\d{3}-?\d{2}$/;
  if (!cpfValido.test(cpf)) {
    return { valido: false, texto: 'CPF deve estar no formato: XXX.XXX.XXX-XX' };
  }
  return { valido: true, texto: '' };
}

function validaSenha(senha) {
  const senhaValida = /(\d){7}(!| @ | ?){2}/;
  if (!senhaValida.test(senha)) {
    return { valido: false, texto: 'A senha deve ter no mínimo 7 dígitos, aém de 2 caracteres entre especiais (!, ?, @)' };
  }
  return { valido: true, texto: '' };
}

export { validaCPF, validaSenha };
