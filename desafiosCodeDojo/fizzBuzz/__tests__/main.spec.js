import { fizzBuzz } from "../src/main";

describe("teste de fizzbuz", () => {
  it("Verifica divisao por 3", () => {
    expect(fizzBuzz(3)).toBe("Fizz");
  });
  it("verifica divisao por 5", () => {
    expect(fizzBuzz(5)).toBe("Buzz");
  });
  it("verifica divisao por 3 e 5", () => {
    expect(fizzBuzz(15)).toBe("FizzBuzz");
  });
});
