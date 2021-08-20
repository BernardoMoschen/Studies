import React from 'react';
import { PropTypes } from 'prop-types';
import DadosPessoais from '../DadosPessoais';
import DadosUsuario from '../DadosUsuario';

function FormularioCadastro({ aoEnviar, validarCPF }) {
  return (
    <>
      <DadosPessoais validarCPF={validarCPF} aoEnviar={aoEnviar} />
      <DadosUsuario />
    </>
  );
}

FormularioCadastro.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
  validarCPF: PropTypes.func.isRequired,
};

export default FormularioCadastro;
