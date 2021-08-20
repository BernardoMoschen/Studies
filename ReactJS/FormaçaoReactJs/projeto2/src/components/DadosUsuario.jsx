import { Button, TextField } from '@material-ui/core';
import React from 'react';

function DadosUsuario() {
  return (
    <form>
      <TextField
        id="email"
        label="email"
        variant="outlined"
        margin="normal"
        fullWidth
        type="email"
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

export default DadosUsuario;
