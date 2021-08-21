import React from 'react';
import { PropTypes } from 'prop-types';
import { Button, TextField } from '@material-ui/core';

function DadosUsuario({ aoEnviar }) {
  return (
    <form onSubmit={(event) => {
      event.preventDefault();
      aoEnviar();
    }}
    >
      <TextField
        id="email"
        label="email"
        type="email"
        required
        variant="outlined"
        margin="normal"
        fullWidth
      />
      <TextField
        id="senha"
        label="senha"
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
};

export default DadosUsuario;
