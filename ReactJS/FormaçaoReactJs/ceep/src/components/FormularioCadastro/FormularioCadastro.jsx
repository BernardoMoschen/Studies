import React, { Component } from "react";
import "./Style.css"

export class FormularioCadastro extends Component {
  render() {
    return (
      <section>
        <form>
          <input type="text" placeholder="Título" />
          <textarea placeholder="Escreva sua nota..." />
          <button>Criar nota</button>
        </form>
      </section>
    );
  }
}

export default FormularioCadastro;
