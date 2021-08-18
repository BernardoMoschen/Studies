import React, { useState } from 'react';
import {
  TextField, Button, Switch, FormControlLabel,
} from '@material-ui/core';

function FormularioCadastro() {
  const [nome, setNome] = useState('');
  return (
    <form onSubmit={(event) => {
      event.preventDefault();
    }}
    >
      <TextField
        onChange={(event) => {
          setNome(event.target.value);
          console.log(nome);
        }}
        id="nome"
        label="Nome"
        variant="outlined"
        margin="normal"
        fullWidth
      />

      <TextField
        id="sobrenome"
        label="Sobrenome"
        variant="outlined"
        margin="normal"
        fullWidth
      />

      <TextField
        id="cpf"
        label="CPF"
        variant="outlined"
        margin="normal"
        fullWidth
      />

      <FormControlLabel control={<Switch name="promocoes" color="primary" defaultChecked />} label="promoções" />

      <FormControlLabel control={<Switch name="novidades" color="primary" defaultChecked />} label="novidades" />

      <Button type="submit" variant="contained" color="primary">
        Cadastrar
      </Button>
    </form>
  );
}

export default FormularioCadastro;
