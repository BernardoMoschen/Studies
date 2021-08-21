import React, { useState, useEffect } from 'react';
import { PropTypes } from 'prop-types';
import {
  Step, StepLabel, Stepper, Typography,
} from '@material-ui/core';
import DadosPessoais from './DadosPessoais';
import DadosUsuario from './DadosUsuario';
import DadosEntrega from './DadosEntrega';

function FormularioCadastro({ aoEnviar, validacoes }) {
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
    <DadosUsuario aoEnviar={coletaDados} validacoes={validacoes} />,
    <DadosPessoais aoEnviar={coletaDados} validacoes={validacoes} />,
    <DadosEntrega aoEnviar={coletaDados} validacoes={validacoes} />,
    <Typography variant="h5">Obrigado pelo Cadastro!</Typography>,
  ];

  useEffect(() => {
    if (etapaAtual === formularios.length - 1) {
      aoEnviar(dadosColetados);
    }
  });

  return (
    <>
      <Stepper activeStep={etapaAtual}>
        <Step>
          <StepLabel>
            Login
          </StepLabel>
        </Step>
        <Step>
          <StepLabel>
            Pessoal
          </StepLabel>
        </Step>
        <Step>
          <StepLabel>
            Entrega
          </StepLabel>
        </Step>
        <Step>
          <StepLabel>
            Finalização
          </StepLabel>
        </Step>
      </Stepper>
      {formularios[etapaAtual]}
    </>
  );
}

FormularioCadastro.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
  validacoes: PropTypes.func.isRequired,
};

export default FormularioCadastro;
