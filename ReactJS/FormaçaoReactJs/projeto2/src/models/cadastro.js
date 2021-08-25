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
    console.log(senha);
    return { valido: false, texto: 'A senha deve ter no mínimo 7 dígitos.' };
  }
  return { valido: true, texto: '' };
}

export { validaCPF, validaSenha };
