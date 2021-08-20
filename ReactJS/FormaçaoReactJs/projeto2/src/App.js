/* eslint-disable react/jsx-filename-extension */
import React from 'react';

import './App.css';
import { Container, Typography } from '@material-ui/core';
import FormularioCadastro from './components/FormularioCadastro/FormularioCadastro';
import 'fontsource-roboto';

function validaCPF(cpf) {
  const cpfVálido = /^\d{3}.?\d{3}.?\d{3}-?\d{2}$/;
  if (!cpfVálido.test(cpf)) {
    return { valido: false, texto: 'CPF deve estar no formato: XXX.XXX.XXX-XX' };
  }
  return { valido: true, texto: '' };
}

function App() {
  return (
    <Container component="article" maxWidth="sm">
      <Typography variant="h3" component="h1" align="center">Formulário Cadastro</Typography>
      <FormularioCadastro validarCPF={validaCPF} />
    </Container>
  );
}

export default App;
