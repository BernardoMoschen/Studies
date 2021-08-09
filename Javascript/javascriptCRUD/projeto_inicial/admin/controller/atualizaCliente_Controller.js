// eslint-disable-next-line import/extensions
import { detalhaCliente } from '../service/cliente_service.js';

const id = new URL(window.location).searchParams.get('id');
const inputNome = document.querySelector('[data-nome]');
const inputEmail = document.querySelector('[data-email]');

detalhaCliente(id).then((dados) => {
  inputNome.value = dados.nome;
  inputEmail.value = dados.email;
});
