var mensagem = "Alfabeto"; //prompt('Digite sua mensagem: ')
var codificada = "";
alert("Hey");
verificamensagem("Alfabeto");
function verificamensagem(mensagem) {
  for (i = 0; i < mensagem.lenght(); i++) {
    letra = mensagem.charAt(i);
    console.log(letra);
    if ("ABC".includes(letra.toUpperCase())) {
      escolhida = "ABC";
      num = escolhida.indexOf(letra);
      total = num * 2;
      codificada + total;
    } else if ("DEF".includes(letra.toUpperCase())) {
      escolhida = "DEF";
      num = index0f(letra);
      codificada += 3 * num;
    } else if ("GHI".includes(letra.toUpperCase())) {
      escolhida = "GHI";
      num = index0f(letra);
      codificada += 4 * num;
    } else if ("JKL".includes(letra.toUpperCase())) {
      escolhida = "JKL";
      num = index0f(letra);
      codificada += 5 * num;
    } else if ("MNO".includes(letra.toUpperCase())) {
      escolhida = "MNO";
      num = index0f(letra);
      codificada += 6 * num;
    } else if (letra.toUpperCase().includes("PQRS")) {
      escolhida = "PQRS";
      num = index0f(letra);
      codificada += 7 * num;
    } else if (letra.toUpperCase().includes("TUV")) {
      escolhida = "TUV";
      num = index0f(letra);
      codificada += 8 * num;
    } else if ("WXYZ".includes(letra.toUpperCase())) {
      escolhida = "WXYZ";
      num = index0f(letra);
      codificada += 9 * num;
    } else if (" ".includes(letra.toUpperCase())) {
      num = index0f(letra);
      codificada += 0;
    }
  }
}
alert(codificada);
