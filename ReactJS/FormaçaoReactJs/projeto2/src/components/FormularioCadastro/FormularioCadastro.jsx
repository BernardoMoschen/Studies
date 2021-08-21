import React, { useState, useEffect } from 'react';
import { PropTypes } from 'prop-types';
import DadosPessoais from './DadosPessoais';
import DadosUsuario from './DadosUsuario';
import DadosEntrega from './DadosEntrega';

function FormularioCadastro({ aoEnviar, validarCPF }) {
  const [etapaAtual, setEtapaAtual] = useState(0);
  const [dadosColetados, setDados] = useState({});

  function proximaEtapa() {
    setEtapaAtual(etapaAtual + 1);
  }
  function coletaDados(dados) {
    setDados({ ...dadosColetados, ...dados });
    proximaEtapa();
  }
  const formularios = [
    <DadosUsuario aoEnviar={coletaDados} />,
    <DadosPessoais aoEnviar={coletaDados} validarCPF={validarCPF} />,
    <DadosEntrega aoEnviar={coletaDados} />,
  ];

  useEffect(() => {
    if (etapaAtual === formularios.length) {
      aoEnviar(dadosColetados);
    }
  });

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
