import React, { useState } from 'react';
import { PropTypes } from 'prop-types';
import { Button, TextField } from '@material-ui/core';

function DadosUsuario({ aoEnviar, validacoes }) {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [erros, setErros] = useState({ senha: { valido: true, texto: '' } });

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
        Cadastrar

      </Button>
    </form>
  );
}

DadosUsuario.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
  validacoes: PropTypes.func.isRequired,
};

export default DadosUsuario;
