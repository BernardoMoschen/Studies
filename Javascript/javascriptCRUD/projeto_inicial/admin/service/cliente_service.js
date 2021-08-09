const listaClientes = () => fetch('http://localhost:3000/profile').then((resposta) => resposta.json());

const criaCliente = (nome, email) => fetch('http://localhost:3000/profile', {
  method: 'POST',
  headers: {
    'Content-type': 'application/json',
  },
  body: JSON.stringify({
    nome, email,
  }),
}).then((resposta) => resposta.body);

const removeCLiente = (id) => fetch(`http://localhost:3000/profile${id}`, {
  method: 'DELETE',
});

export { listaClientes, criaCliente, removeCLiente };
