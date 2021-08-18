import React from 'react';

import './App.css';
import { Container } from '@material-ui/core';
import FormularioCadastro from './components/FormularioCadastro/FormularioCadastro';

function App() {
  return (
    <Container component="article" maxWidth="sm">
      <h1>Formulário Cadastro</h1>
      <FormularioCadastro />
    </Container>
  );
}

export default App;
