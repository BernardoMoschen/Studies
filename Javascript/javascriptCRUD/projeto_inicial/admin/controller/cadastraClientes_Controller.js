// eslint-disable-next-line import/extensions
import { criaCliente } from '../service/cliente_service.js';

const formulario = document.querySelector('[data-form]');

formulario.addEventListener('submit', async (evento) => {
  evento.preventDefault();
  const nome = evento.target.querySelector('[data-nome]').value;
  const email = evento.target.querySelector('[data-email]').value;

  await criaCliente(nome, email);
  window.location.href = '../telas/cadastro_concluido.html';
});
