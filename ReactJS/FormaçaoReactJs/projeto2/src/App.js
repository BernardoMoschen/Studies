/* eslint-disable react/jsx-filename-extension */
import React from 'react';

import './App.css';
import { Container, Typography } from '@material-ui/core';
import FormularioCadastro from './components/FormularioCadastro/FormularioCadastro';
import 'fontsource-roboto';

function App() {
  return (
    <Container component="article" maxWidth="sm">
      <Typography variant="h3" component="h1" align="center">Formulário Cadastro</Typography>
      <FormularioCadastro />
    </Container>
  );
}

export default App;
