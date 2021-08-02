import React, { Component } from "react";
import "./Style.css";

export class FormularioCadastro extends Component {
  render() {
    return (
      <section>
        <form className="form-cadastro">
          <input
            type="text"
            placeholder="Título"
            className="form-cadastro_input"
          />
          <textarea
            placeholder="Escreva sua nota..."
            className="form-cadastro_input"
          />
          <button className="form-cadastro_input form-cadastro_submit">
            Criar nota
          </button>
        </form>
      </section>
    );
  }
}

export default FormularioCadastro;
