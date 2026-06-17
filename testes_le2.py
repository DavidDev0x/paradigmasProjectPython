from le2.plp.expressions2.exemplo1 import Exemplo1
from le2.plp.expressions2.exemplo2 import Exemplo2
from le2.plp.expressions2.exemplo3 import Exemplo3
from le2.plp.expressions2.exemplo4 import Exemplo4
from le2.plp.expressions2.exemplo5 import Exemplo5
from le2.plp.expressions2.exemplos import Exemplos


def main() -> None:
    esperados = ["2", "3", "6", "4", "8"]
    exemplos = [Exemplo1, Exemplo2, Exemplo3, Exemplo4, Exemplo5]
    for cls, esperado in zip(exemplos, esperados):
        tipo_valido, resultado = cls.executar()
        assert tipo_valido is True, f"{cls.__name__}: tipo deveria ser válido"
        assert resultado == esperado, f"{cls.__name__}: esperado {esperado}, obtido {resultado}"

    from le2.plp.expressions2.expression.valor_inteiro import ValorInteiro
    try:
        ValorInteiro(True)
    except TypeError:
        pass
    else:
        raise AssertionError("ValorInteiro(True) deveria ser rejeitado para evitar bool como int.")

    resultados = Exemplos.executar_todos()
    falhas = [r for r in resultados if not r.ok]
    if falhas:
        for falha in falhas:
            print(falha)
        raise AssertionError("Há exemplos falhando.")
    print("Todos os testes da LE2 passaram.")


if __name__ == "__main__":
    main()
