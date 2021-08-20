import React from 'react';
import { PropTypes } from 'prop-types';
import DadosPessoais from './DadosPessoais';
import DadosUsuario from './DadosUsuario';
import DadosEntrega from './DadosEntrega';

function FormularioCadastro({ aoEnviar, validarCPF }) {
  return (
    <>
      <DadosPessoais validarCPF={validarCPF} aoEnviar={aoEnviar} />
      <DadosUsuario />
      <DadosEntrega />
    </>
  );
}

FormularioCadastro.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
  validarCPF: PropTypes.func.isRequired,
};

export default FormularioCadastro;
