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

  function envioValido() {
    // eslint-disable-next-line no-restricted-syntax
    for (const campo in erros) {
      if (!erros[campo].valido) {
        return false;
      }
    }
    return true;
  }
  return [erros, validarCampos, envioValido];
}

export default useErros;
