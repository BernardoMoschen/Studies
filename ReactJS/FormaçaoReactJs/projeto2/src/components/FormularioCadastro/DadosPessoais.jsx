import React, { useState, useContext } from 'react';
import { PropTypes } from 'prop-types';
import {
  TextField, Button, Switch, FormControlLabel,
} from '@material-ui/core';
import ValidacoesCadastro from '../../contexts/ValidacoesCadastro';
import useErros from '../../hooks/useErros';

function DadosPessoais({ aoEnviar }) {
  const [nome, setNome] = useState('');
  const [sobrenome, setSobrenome] = useState('');
  const [cpf, setCpf] = useState('');
  const [promocoes, setPromocoes] = useState(true);
  const [novidades, setNovidades] = useState(true);
  const validacoes = useContext(ValidacoesCadastro);
  const [erros, validarCampos] = useErros(validacoes);

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
        aoEnviar({
          nome, sobrenome, cpf, promocoes, novidades,
        });
      }
    }}
    >
      <TextField
        value={nome}
        onChange={(event) => {
          setNome(event.target.value);
        }}
        onBlur={validarCampos}
        error={!erros.nome.valido}
        helperText={erros.nome.texto}
        id="nome"
        label="Nome"
        name="nome"
        required
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
        name="sobrenome"
        required
        type="text"
        variant="outlined"
        margin="normal"
        fullWidth
      />

      <TextField
        onChange={(event) => {
          setCpf(event.target.value);
        }}
        onBlur={validarCampos}
        error={!erros.cpf.valido}
        helperText={erros.cpf.texto}
        id="cpf"
        name="cpf"
        label="CPF"
        required
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
        Próximo
      </Button>
    </form>
  );
}

DadosPessoais.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
};

export default DadosPessoais;
