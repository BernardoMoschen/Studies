import React, { useState } from 'react';
import { PropTypes } from 'prop-types';
import DadosPessoais from './DadosPessoais';
import DadosUsuario from './DadosUsuario';
import DadosEntrega from './DadosEntrega';

function FormularioCadastro({ aoEnviar, validarCPF }) {
  const [etapaAtual, setEtapaAtual] = useState(0);

  function proximaEtapa() {
    setEtapaAtual(etapaAtual + 1);
  }
  const formularios = [
    <DadosUsuario aoEnviar={proximaEtapa} />,
    <DadosPessoais aoEnviar={proximaEtapa} validarCPF={validarCPF} />,
    <DadosEntrega aoEnviar={aoEnviar} />,
  ];

  return (
    <>
      {formularios[etapaAtual]}
    </>
  );
}

FormularioCadastro.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
  validarCPF: PropTypes.func.isRequired,
};

export default FormularioCadastro;
