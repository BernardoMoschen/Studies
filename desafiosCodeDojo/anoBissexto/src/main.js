export function verificaAnoPor4(ano) {
  // Opção 1
  return ano % 4 == 0;
  /*
  // Opção 2
  if (ano % 4 == 0) {
    return true;
  }
  return false;
  */
  /*
  Opção 3
  if (ano % 4 == 0) {
    return true;
  } else {
    return false;
  }
  */
  // Opção 4
  // return ano % 4 == 0 ? true : false;
}
export function verificaAnoPor100(ano) {
  if (ano % 100 == 0) {
    return true;
  }
  return false;
  // return ano % 100 == 0 ? true : false;
}
export function verificaAnoPor400(ano) {
  return ano % 400 == 0 ? true : false;
}

export function verificaAnoBissexto(ano) {
  if (verificaAnoPor4(ano) && !verificaAnoPor100(ano)) {
    return true;
  }
  if (verificaAnoPor400(ano)) {
    return true;
  }
  return false;
}
