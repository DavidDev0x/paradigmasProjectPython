from le1.exemplos import Exemplos
from le1.plp.expressions1.expression import ErroTipo, ExpSoma, ValorBooleano, ValorInteiro


def main() -> None:
    resultados = Exemplos.executar_todos()
    assert all(resultado["ok"] for resultado in resultados), resultados

    try:
        ValorInteiro(True)
    except ErroTipo:
        pass
    else:
        raise AssertionError("ValorInteiro(True) deveria lançar ErroTipo")

    try:
        ExpSoma(ValorBooleano(True), ValorInteiro(2)).avaliar()
    except ErroTipo:
        pass
    else:
        raise AssertionError("True + 2 deveria lançar ErroTipo")

    print("Todos os testes passaram.")


if __name__ == "__main__":
    main()
