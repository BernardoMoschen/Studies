// eslint-disable-next-line import/extensions
import { detalhaCliente, atualizaCliente } from '../service/cliente_service.js';

const id = new URL(window.location).searchParams.get('id');
const inputNome = document.querySelector('[data-nome]');
const inputEmail = document.querySelector('[data-email]');

detalhaCliente(id).then((dados) => {
  inputNome.value = dados.nome;
  inputEmail.value = dados.email;
});

const formulario = document.querySelector('[data-form]');
formulario.addEventListener('submit', (evento) => {
  evento.preventDefault();
  atualizaCliente(id, inputNome.value, inputEmail.value).then(() => {
    window.location.href = '../telas/edicao_concluida.html';
  });
});
