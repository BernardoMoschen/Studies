import React from 'react';

import { Button, TextField } from '@material-ui/core';
import { PropTypes } from 'prop-types';

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
        variant="outlined"
        margin="normal"
        type="email"
        fullWidth
      />
      <TextField
        id="senha"
        label="senha"
        variant="outlined"
        margin="normal"
        type="password"
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
