// eslint-disable-next-line import/extensions
import { listaClientes, removeCLiente } from '../service/cliente_service.js';

const criaNovaLinha = (nome, email, id) => {
  const linhaNovoCliente = document.createElement('tr');
  const conteudo = `<td class="td" data-td>${nome}</td>
                  <td>${email}</td>
                  <td>
                      <ul class="tabela__botoes-controle">
                          <li><a href="../telas/edita_cliente.html?id=${id}" class="botao-simples botao-simples--editar">Editar</a></li>
                          <li><button class="botao-simples botao-simples--excluir" type="button">Excluir</button></li>
                      </ul>
                  </td>`;

  linhaNovoCliente.innerHTML = conteudo;
  linhaNovoCliente.dataset.id = id;
  return linhaNovoCliente;
};

const tabela = document.querySelector('[data-tabela]');

tabela.addEventListener('click', (evento) => {
  const botaoExcluir = evento.target.className === 'botao-simples botao-simples--excluir';
  if (botaoExcluir) {
    const linhaCliente = evento.target.closest('[data-id]');
    const { id } = linhaCliente.dataset;
    removeCLiente(id).then(() => {
      linhaCliente.remove();
    });
  }
});

listaClientes().then((data) => {
  data.forEach((element) => {
    tabela.appendChild(criaNovaLinha(element.nome, element.email, element.id));
  });
});
