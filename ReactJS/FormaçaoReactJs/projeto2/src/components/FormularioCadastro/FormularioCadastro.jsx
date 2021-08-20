import React, { useState } from 'react';
import { PropTypes } from 'prop-types';
import { Typography } from '@material-ui/core';
import DadosPessoais from './DadosPessoais';
import DadosUsuario from './DadosUsuario';
import DadosEntrega from './DadosEntrega';

function FormularioCadastro({ validarCPF }) {
  const [etapaAtual, setEtapaAtual] = useState(0);

  function proximaEtapa() {
    setEtapaAtual(etapaAtual + 1);
  }

  function formularioAtual(etapa) {
    switch (etapa) {
      case 0:
        return <DadosUsuario aoEnviar={proximaEtapa} />;
      case 1:
        return <DadosPessoais aoEnviar={proximaEtapa} validarCPF={validarCPF} />;
      case 2:
        return <DadosEntrega />;
      default:
        return <Typography>Erro durante a seleção do formulário.</Typography>;
    }
  }

  return (
    <>
      {formularioAtual(etapaAtual)}
    </>
  );
}

FormularioCadastro.propTypes = {
  validarCPF: PropTypes.func.isRequired,
};

export default FormularioCadastro;
