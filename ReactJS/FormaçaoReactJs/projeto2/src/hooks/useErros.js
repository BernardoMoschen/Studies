/* eslint-disable guard-for-in */
import { useState } from 'react';

function criarEstadoInicial(validacoes) {
  const estadoInicial = {};
  // eslint-disable-next-line no-restricted-syntax
  for (const campo in validacoes) {
    estadoInicial[campo] = { valido: true, texto: '' };
  }
  return estadoInicial;
}

function useErros(validacoes) {
  const estadoInicial = criarEstadoInicial(validacoes);
  const [erros, setErros] = useState(estadoInicial);

  function validarCampos(event) {
    const { name, value } = event.target;
    const novoEstado = { ...erros };
    novoEstado[name] = validacoes[name](value);
    setErros(novoEstado);
  }

  return [erros, validarCampos];
}

export default useErros;
