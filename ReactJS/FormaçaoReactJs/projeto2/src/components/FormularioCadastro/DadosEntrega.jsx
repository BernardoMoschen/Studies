import { TextField, Button } from '@material-ui/core';
import React, { useState } from 'react';
import { PropTypes } from 'prop-types';

function DadosEntrega({ aoEnviar }) {
  const [cep, setCEP] = useState('');
  const [endereço, setEndereco] = useState('');
  const [numero, setNumero] = useState('');
  const [estado, setEstado] = useState('');
  const [cidade, setCidade] = useState('');

  return (
    <form onSubmit={(event) => {
      event.preventDefault();
      aoEnviar({
        cep, endereço, numero, estado, cidade,
      });
    }}
    >
      <TextField
        value={cep}
        onChange={(event) => {
          setCEP(event.target.value);
        }}
        id="CEP"
        label="CEP"
        type="number"
        variant="outlined"
        margin="normal"
      />
      <TextField
        value={endereço}
        onChange={(event) => {
          setEndereco(event.target.value);
        }}
        id="endereço"
        label="Endereço"
        type="text"
        variant="outlined"
        margin="normal"
        fullWidth
      />
      <TextField
        value={numero}
        onChange={(event) => {
          setNumero(event.target.value);
        }}
        id="numero"
        label="Número"
        type="number"
        variant="outlined"
        margin="normal"
      />
      <TextField
        value={estado}
        onChange={(event) => {
          setEstado(event.target.value);
        }}
        id="estado"
        label="Estado"
        type="text"
        variant="outlined"
        margin="normal"
      />
      <TextField
        value={cidade}
        onChange={(event) => {
          setCidade(event.target.value);
        }}
        id="cidade"
        label="Cidade"
        type="text"
        variant="outlined"
        margin="normal"
      />
      <Button
        type="submit"
        variant="contained"
        color="primary"
        fullWidth
      >
        Finalizar Cadastro
      </Button>
    </form>
  );
}

DadosEntrega.propTypes = {
  aoEnviar: PropTypes.func.isRequired,
};

export default DadosEntrega;
