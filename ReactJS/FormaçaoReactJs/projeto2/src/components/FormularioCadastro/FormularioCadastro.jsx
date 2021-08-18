import React, { useState } from 'react';
import {
  TextField, Button, Switch, FormControlLabel,
} from '@material-ui/core';

function FormularioCadastro() {
  const [nome, setNome] = useState('');
  const [sobrenome, setSobrenome] = useState('');

  return (
    <form onSubmit={(event) => {
      event.preventDefault();
      console.log(nome, sobrenome);
    }}
    >
      <TextField
        value={nome}
        onChange={(event) => {
          let tempNome = event.target.value;
          if (tempNome.length >= 3) {
            tempNome = tempNome.substr(0, 3);
            console.log(tempNome);
          }
          setNome(tempNome);
        }}
        id="nome"
        label="Nome"
        variant="outlined"
        margin="normal"
        fullWidth
      />

      <TextField
        onChange={(event) => {
          setSobrenome(event.target.value);
        }}
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

      <FormControlLabel
        control={(
          <Switch
            name="promocoes"
            color="primary"
            defaultChecked
          />
        )}
        label="promoções"
      />

      <FormControlLabel
        control={(
          <Switch
            name="novidades"
            color="primary"
            defaultChecked
          />
        )}
        label="novidades"
      />

      <Button
        type="submit"
        variant="contained"
        color="primary"
      >
        Cadastrar
      </Button>
    </form>
  );
}

export default FormularioCadastro;
