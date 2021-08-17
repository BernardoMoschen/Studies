import React from 'react';
import Button from '@material-ui/core/Button';

function FormularioCadastro() {
  return (
    <form>
      <label htmlFor="nome">
        Nome
        <input id="nome" type="text" />
      </label>

      <label htmlFor="sobrenome">
        Sobrenome
        <input id="sobrenome" type="text" />
      </label>

      <label htmlFor="cpf">
        CPF
        <input id="cpf" type="text" />
      </label>

      <label htmlFor="promocoes">
        Promoções
        <input id="promocoes" type="checkbox" />
      </label>

      <label htmlFor="novidades">
        Novidades
        <input id="novidades" type="checkbox" />
      </label>

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
