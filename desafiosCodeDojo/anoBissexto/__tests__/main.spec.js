import {
  verificaAnoPor4,
  verificaAnoPor100,
  verificaAnoPor400,
  verificaAnoBissexto
} from "../src/main";

describe("teste ano bisexto", () => {
  it("Verifica se o ano é divisivel por 4 - 2020 é divisivel por 4", () => {
    expect(verificaAnoPor4(2020)).toBe(true);
  });
  it("Verifica se o ano é divisivel por 4 - 2019 NÃO é divisivel por 4", () => {
    expect(verificaAnoPor4(2019)).toBe(false);
  });
  it("Verifica se o ano é divisivel por 100 - 2000 é divisivel por 100", () => {
    expect(verificaAnoPor100(2000)).toBe(true);
  });
  it("Verifica se o ano é divisivel por 100 - 2020 NÃO é divisivel por 100", () => {
    expect(verificaAnoPor100(2020)).toBe(false);
  });
  it("Verifica se o ano é divisivel por 400 - 2020 NÃO é divisivel por 400", () => {
    expect(verificaAnoPor400(2020)).toBe(false);
  });
  it("Verifica se o ano é divisivel por 400 - 1600 é divisivel por 400", () => {
    expect(verificaAnoPor400(1600)).toBe(true);
  });

  it("Verifica se o ano é bissexto - 1600 é bissexto", () => {
    expect(verificaAnoBissexto(1600)).toBe(true);
  });
  it("Verifica se o ano é bissexto - 1700 NÃO é bissexto", () => {
    expect(verificaAnoBissexto(1700)).toBe(false);
  });
  it("Verifica se o ano é bissexto - 4 é bissexto", () => {
    expect(verificaAnoBissexto(4)).toBe(true);
  });
  it("Verifica se o ano é bissexto - 1604 é bissexto", () => {
    expect(verificaAnoBissexto(1604)).toBe(true);
  });
  it("Verifica se o ano é bissexto - 1742 NÃO é bissexto", () => {
    expect(verificaAnoBissexto(1742)).toBe(false);
  });
  it("Verifica se o ano é bissexto - 1732 é bissexto", () => {
    expect(verificaAnoBissexto(1732)).toBe(true);
  });
  it("Verifica se o ano é bissexto - 1889 NÃO é bissexto", () => {
    expect(verificaAnoBissexto(1889)).toBe(false);
  });
  it("Verifica se o ano é bissexto - 1951 NÃO é bissexto", () => {
    expect(verificaAnoBissexto(1951)).toBe(false);
  });
  it("Verifica se o ano é bissexto - 2011 NÃO é bissexto", () => {
    expect(verificaAnoBissexto(2011)).toBe(false);
  });
  it("Verifica se o ano é bissexto - 1888 é bissexto", () => {
    expect(verificaAnoBissexto(1888)).toBe(true);
  });
  it("Verifica se o ano é bissexto - 1944 é bissexto", () => {
    expect(verificaAnoBissexto(1944)).toBe(true);
  });
  it("Verifica se o ano é bissexto - 2008 é bissexto", () => {
    expect(verificaAnoBissexto(2008)).toBe(true);
  });
  it("Verifica se o ano é bissexto - 100 NÃO é bissexto", () => {
    expect(verificaAnoBissexto(100)).toBe(false);
  });
});
