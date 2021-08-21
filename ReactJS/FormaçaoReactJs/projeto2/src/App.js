/* eslint-disable react/jsx-filename-extension */
import React from 'react';
import './App.css';
import { Container, Typography } from '@material-ui/core';
import FormularioCadastro from './components/FormularioCadastro/FormularioCadastro';
import 'fontsource-roboto';
import { validaCPF, validaSenha } from './models/cadastro';

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
      <FormularioCadastro
        aoEnviar={envioForm}
        validacoes={{ cpf: validaCPF, senha: validaSenha }}
      />
    </Container>
  );
}

export default App;
