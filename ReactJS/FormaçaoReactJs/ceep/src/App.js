import React, { Component } from 'react';
import ListaDeNotas from './components/ListaDeNotas';
import FormularioCadastro from './components/FormularioCadastro';
import ListaDeCategorias from './components/ListaDeCategorias';
import './assets/App.css';
import './assets/index.css';

class App extends Component {
  constructor() {
    super();
  }
  render() {
    return (   
      <section className="conteudo">
        <FormularioCadastro
        categorias={this.state.categorias}
         criarNota={this.criarNota.bind(this)}
         />
        <main className="conteudo-principal">
        <ListaDeCategorias 
          adicionarCategoria={this.adicionarCategoria.bind(this)}
          categorias={this.state.categorias}/>
        <ListaDeNotas
          deletarNota={this.deletarNota.bind(this)}
          notas={this.state.notas}
          />
          </main>
      </section>
    );
  }
}

// new ListaDeNotas({notas:this.notas})
export default App;
