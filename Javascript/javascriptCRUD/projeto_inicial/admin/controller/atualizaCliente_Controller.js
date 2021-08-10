// eslint-disable-next-line import/extensions
import { detalhaCliente, atualizaCliente } from '../service/cliente_service.js';

(async () => {
  const id = new URL(window.location).searchParams.get('id');
  const inputNome = document.querySelector('[data-nome]');
  const inputEmail = document.querySelector('[data-email]');
  try {
    const dados = await detalhaCliente(id);
    inputNome.value = dados.nome;
    inputEmail.value = dados.email;
  } catch (erro) {
    console.log(erro);
    window.location.href = '../telas/erro.html';
  }

  const formulario = document.querySelector('[data-form]');
  formulario.addEventListener('submit', async (evento) => {
    evento.preventDefault();
    try {
      await atualizaCliente(id, inputNome.value, inputEmail.value);
      window.location.href = '../telas/edicao_concluida.html';
    } catch (erro) {
      console.log(erro);
      window.location.href = '../telas/erro.html';
    }
  });
})();
