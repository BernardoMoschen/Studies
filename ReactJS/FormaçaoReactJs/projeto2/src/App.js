/* eslint-disable react/jsx-filename-extension */
import React from 'react';
import './App.css';
import { Container, Typography } from '@material-ui/core';
import FormularioCadastro from './components/FormularioCadastro/FormularioCadastro';
import 'fontsource-roboto';
import { validaCPF, validaNome, validaSenha } from './models/cadastro';
import ValidacoesCadastro from './contexts/ValidacoesCadastro';

function envioForm(dadosCadastro) {
  console.log(dadosCadastro);
}

function App() {
  return (
    <Container component="article" maxWidth="sm">
      <Typography
        variant="h3"
        component="h1"
        align="center"
      >
        Formulário Cadastro
      </Typography>
      <ValidacoesCadastro.Provider value={{ cpf: validaCPF, senha: validaSenha, nome: validaNome }}>
        <FormularioCadastro aoEnviar={envioForm} />
      </ValidacoesCadastro.Provider>
    </Container>
  );
}

export default App;
