from __future__ import annotations

from typing import Any

from le1.plp.expressions1 import Programa
from le1.plp.expressions1.expression import (
    ErroTipo,
    ExpAnd,
    ExpConcat,
    ExpEquals,
    ExpLength,
    ExpMenos,
    ExpNot,
    ExpOr,
    ExpSoma,
    ExpSub,
    Expressao,
    ValorBooleano,
    ValorInteiro,
    ValorString,
)


class Exemplos:
    @staticmethod
    def executar(exp: Expressao) -> str:
        programa = Programa(exp)
        if programa.checa_tipo():
            return str(programa.executar())
        print("Erro de tipo")
        return "Erro de tipo"

    @staticmethod
    def executar_todos() -> list[dict[str, Any]]:
        casos: list[tuple[str, Expressao, str]] = [
            (
                "soma e subtração: (-4 + 12) - 3",
                ExpSub(ExpSoma(ValorInteiro(-4), ValorInteiro(12)), ValorInteiro(3)),
                "5",
            ),
            (
                "menos unário: -5",
                ExpMenos(ValorInteiro(5)),
                "-5",
            ),
            (
                "length e soma: length('abc') + 3",
                ExpSoma(ExpLength(ValorString("abc")), ValorInteiro(3)),
                "6",
            ),
            (
                "conjunção: true and false",
                ExpAnd(ValorBooleano(True), ValorBooleano(False)),
                "false",
            ),
            (
                "disjunção: true or false",
                ExpOr(ValorBooleano(True), ValorBooleano(False)),
                "true",
            ),
            (
                "negação: not false",
                ExpNot(ValorBooleano(False)),
                "true",
            ),
            (
                "igualdade: 'abc' == 'abc'",
                ExpEquals(ValorString("abc"), ValorString("abc")),
                "true",
            ),
            (
                "concatenação: 'Carreta' ++ ' furacao ' ++ 'do brega'",
                ExpConcat(
                    ExpConcat(ValorString("Carreta"), ValorString(" furacao ")),
                    ValorString("do brega"),
                ),
                "Carreta furacao do brega",
            ),
        ]

        erros: list[tuple[str, Expressao]] = [
            ("erro: 1 + true", ExpSoma(ValorInteiro(1), ValorBooleano(True))),
            ("erro: 'a' ++ 2", ExpConcat(ValorString("a"), ValorInteiro(2))),
            ("erro: length(10)", ExpLength(ValorInteiro(10))),
            ("erro: not 1", ExpNot(ValorInteiro(1))),
            ("erro: true and 1", ExpAnd(ValorBooleano(True), ValorInteiro(1))),
            ("erro: 1 == true", ExpEquals(ValorInteiro(1), ValorBooleano(True))),
        ]

        resultados: list[dict[str, Any]] = []
        for nome, exp, esperado in casos:
            obtido = Exemplos.executar(exp)
            resultados.append(
                {
                    "caso": nome,
                    "esperado": esperado,
                    "obtido": obtido,
                    "ok": obtido == esperado,
                }
            )

        for nome, exp in erros:
            programa = Programa(exp)
            if programa.checa_tipo():
                try:
                    obtido = str(programa.executar())
                except ErroTipo:
                    obtido = "Erro de tipo"
            else:
                print("Erro de tipo")
                obtido = "Erro de tipo"
            resultados.append(
                {
                    "caso": nome,
                    "esperado": "Erro de tipo",
                    "obtido": obtido,
                    "ok": obtido == "Erro de tipo",
                }
            )

        return resultados


if __name__ == "__main__":
    for resultado in Exemplos.executar_todos():
        status = "OK" if resultado["ok"] else "FALHOU"
        print(f"[{status}] {resultado['caso']} -> {resultado['obtido']}")
