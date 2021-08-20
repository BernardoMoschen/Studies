import { Button, TextField } from '@material-ui/core';
import React from 'react';

function DadosUsuario() {
  return (
    <form>
      <TextField id="email" label="email" type="email" />
      <TextField id="senha" label="senha" type="password" />
      <Button type="submit">Cadastrar</Button>
    </form>
  );
}

export default DadosUsuario;
