import React, { Component } from "react";
import FormularioCadastro from "./components/FormularioCadastro/FormularioCadastro";
import ListaDeNotas from "./components/ListaDeNotas/ListaDeNotas";
import "./assets/App.css";
import './assets/index.css';

export class App extends Component {
  render() {
    return (
      <section>
      <form>
        <input type="text" placeholder="Título" />
        <textarea placeholder="Escreva sua nota..." />
        <button>Criar nota</button>
      </form>
      <FormularioCadastro/>
      <ListaDeNotas />
    </section>
    )
  }
}

export default App;
