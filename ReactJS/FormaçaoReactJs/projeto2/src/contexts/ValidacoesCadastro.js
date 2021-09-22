import React from 'react';

function defaultProvider(dados) {
  console.log(dados);
  return { valido: true, texto: '' };
}
const ValidacoesCadastro = React.createContext(
  { cpf: defaultProvider, senha: defaultProvider, nome: defaultProvider },
);

export default ValidacoesCadastro;
