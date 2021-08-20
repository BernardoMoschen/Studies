import React, { useState } from 'react';
import { PropTypes } from 'prop-types';
import {
  TextField, Button, Switch, FormControlLabel,
} from '@material-ui/core';

function DadosPessoais({ aoEnviar, validarCPF }) {
  const [nome, setNome] = useState('');
  const [sobrenome, setSobrenome] = useState('');
  const [cpf, setCpf] = useState('');
  const [promocoes, setPromocoes] = useState(true);
  const [novidades, setNovidades] = useState(true);
  const [erros, setErros] = useState({ cpf: { valido: true, texto: '' } });

  return (
    <form onSubmit={(event) => {
      event.preventDefault();
      aoEnviar({
        nome, sobrenome, cpf, promocoes, novidades,
      });
    }}
    >
      <TextField
        value={nome}
        onChange={(event) => {
          setNome(event.target.value);
        }}
        id="nome"
        label="Nome"
        type="text"
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
        type="text"
        variant="outlined"
        margin="normal"
        fullWidth
      />

      <TextField
        onChange={(event) => {
          setCpf(event.target.value);
        }}
        onBlur={() => {
          const isValid = validarCPF(cpf);
          setErros({ cpf: isValid });
        }}
        error={!erros.cpf.valido}
        helperText={erros.cpf.texto}
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

DadosPessoais.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
  validarCPF: PropTypes.func.isRequired,
};

export default DadosPessoais;
