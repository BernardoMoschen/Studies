import React, { useState, useContext } from 'react';
import { PropTypes } from 'prop-types';
import { Button, TextField } from '@material-ui/core';
import ValidacoesCadastro from '../../contexts/ValidacoesCadastro';
import useErros from '../../hooks/useErros';

function DadosUsuario({ aoEnviar }) {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const validacoes = useContext(ValidacoesCadastro);
  const [erros, validarCampos, envioValido] = useErros(validacoes);

  return (
    <form onSubmit={(event) => {
      event.preventDefault();
      if (envioValido()) {
        aoEnviar({ email, senha });
      }
    }}
    >
      <TextField
        value={email}
        onChange={(event) => {
          setEmail(event.target.value);
        }}
        id="email"
        label="email"
        type="email"
        name="email"
        required
        variant="outlined"
        margin="normal"
        fullWidth
      />
      <TextField
        value={senha}
        onChange={(event) => {
          setSenha(event.target.value);
        }}
        onBlur={validarCampos}
        error={!erros.senha.valido}
        helperText={erros.senha.texto}
        id="senha"
        label="senha"
        name="senha"
        type="password"
        required
        variant="outlined"
        margin="normal"
        fullWidth
      />
      <Button
        variant="contained"
        color="primary"
        type="submit"
      >
        Próximo

      </Button>
    </form>
  );
}

DadosUsuario.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
};

export default DadosUsuario;
