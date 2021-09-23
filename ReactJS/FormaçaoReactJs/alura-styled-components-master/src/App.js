import React, {useState} from "react";
import { ThemeProvider } from 'styled-components'
import { temaClaro, temaEscuro } from './Components/UI/temas'
import Cabecalho from "./Components/Cabecalho";
import Container from "./Components/Container";
import GlobalStyle from "./Components/GlobalStyle"
import {ButtonTema} from './Components/UI/index'
import SwitchTema from "./Components/SwitchTema"

function App() {
  const [tema, setTema] = useState(true)

  const toggleTema = () => {
    setTema(() => !tema)
  }

   return (
    <ThemeProvider theme={tema ? temaClaro : temaEscuro}>
      <GlobalStyle/>
      <ButtonTema onClick={toggleTema} >
        <SwitchTema tema={tema}/>
      </ButtonTema>
      <Cabecalho />
      <Container />
    </ThemeProvider>
  );
}

export default App;
