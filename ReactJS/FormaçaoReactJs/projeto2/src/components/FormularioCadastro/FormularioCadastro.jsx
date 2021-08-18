import React, { useState } from 'react';
import {
  TextField, Button, Switch, FormControlLabel,
} from '@material-ui/core';

function FormularioCadastro() {
  const [nome, setNome] = useState('');
  const [sobrenome, setSobrenome] = useState('');
  const [cpf, setCpf] = useState('');
  const [promocoes, setPromocoes] = useState(true);
  const [novidades, setNovidades] = useState(true);

  return (
    <form onSubmit={(event) => {
      event.preventDefault();
      console.log(nome, sobrenome, cpf, promocoes, novidades);
    }}
    >
      <TextField
        value={nome}
        onChange={(event) => {
          setNome(event.target.value);
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
        onChange={(event) => {
          setCpf(event.target.value);
        }}
        id="cpf"
        label="CPF"
        variant="outlined"
        margin="normal"
        fullWidth
      />

      <FormControlLabel
        control={(
          <Switch
            onChange={(event) => {
              setPromocoes(event.target.checked);
            }}
            name="promocoes"
            color="primary"
            checked={promocoes}
          />
        )}
        label="promoções"
      />

      <FormControlLabel
        control={(
          <Switch
            onChange={(event) => {
              setNovidades(event.target.checked);
            }}
            name="novidades"
            color="primary"
            checked={novidades}
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
