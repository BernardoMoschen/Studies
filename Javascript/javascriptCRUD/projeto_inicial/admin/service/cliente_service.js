const listaClientes = () => fetch('http://localhost:3000/profile').then((resposta) => resposta.json());

export default listaClientes;
