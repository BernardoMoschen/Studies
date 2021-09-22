import React from 'react'
import imagem from '../assets/img/doguito404.svg'
import '../assets/css/404.css'

export default function Pagina404() {
    return (
        <main className="cointainer flex flex--centro flex--coluna">
            <br/>
            <p className="naoencontrado-texto">
              Ops, essa página não existe!
              </p>
          <img className="doguito-imagem" src={imagem} alt=""/> 
           
        </main>
    )
}
