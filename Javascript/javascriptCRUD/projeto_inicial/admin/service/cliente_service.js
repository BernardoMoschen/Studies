const listaClientes = () => fetch('http://localhost:3000/profile').then((resposta) => {
  if (resposta.ok) {
    return resposta.json();
  }
  throw new Error('Não foi possível listar os clientes.');
});

const criaCliente = (nome, email) => fetch('http://localhost:3000/profile', {
  method: 'POST',
  headers: {
    'Content-type': 'application/json',
  },
  body: JSON.stringify({
    nome, email,
  }),
}).then((resposta) => {
  if (resposta.ok) {
    return resposta.body;
  }
  throw new Error('Não foi possível criar um novo cliente.');
});

const removeCLiente = (id) => fetch(`http://localhost:3000/profile/${id}`, {
  method: 'DELETE',
}).then((resposta) => {
  if (!resposta.ok) {
    throw new Error('Não foi possível remover o cliente.');
  }
});

const detalhaCliente = (id) => fetch(`http://localhost:3000/profile/${id}`).then((resposta) => {
  if (resposta.ok) {
    return resposta.json();
  }
  throw new Error('Não foi possível detalhar o cliente.');
});

const atualizaCliente = (id, nome, email) => fetch(`http://localhost:3000/profile/${id}`, {
  method: 'PUT',
  headers: {
    'Content-type': 'application/json',
  },
  body: JSON.stringify({
    nome,
    email,
  }),
}).then((resposta) => {
  if (resposta.ok) {
    return resposta.json();
  }
  throw new Error('Não foi possível atualizar o cliente.');
});

export {
  listaClientes, criaCliente, removeCLiente, detalhaCliente, atualizaCliente,
};
