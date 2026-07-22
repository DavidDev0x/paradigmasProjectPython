from __future__ import annotations

# Permite executar este arquivo diretamente na IDE sem instalar o pacote.
# Ex.: clicar em Run no PyCharm/VS Code ou usar: python le1/plp/expressions1/Exemplos.py
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from typing import Any

from le1.plp.expressions1 import Programa
from le1.plp.expressions1.expression import (
    ExpAnd,
    ExpConcat,
    ExpLength,
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
        resultados: list[dict[str, Any]] = []

        # -----------------------------
        # 1) -4 + 12 - 3
        # -----------------------------
        exp1: Expressao = ExpSub(
            ExpSoma(
                ValorInteiro(-4),
                ValorInteiro(12),
            ),
            ValorInteiro(3),
        )
        obtido = Exemplos.executar(exp1)
        resultados.append(
            {
                "caso": "1) -4 + 12 - 3",
                "esperado": "5",
                "obtido": obtido,
                "ok": obtido == "5",
            }
        )

        # -----------------------------
        # 2) length("abc") + 3
        # -----------------------------
        exp2: Expressao = ExpSoma(
            ExpLength(ValorString("abc")),
            ValorInteiro(3),
        )
        obtido = Exemplos.executar(exp2)
        resultados.append(
            {
                "caso": '2) length("abc") + 3',
                "esperado": "6",
                "obtido": obtido,
                "ok": obtido == "6",
            }
        )

        # -----------------------------
        # 3) true and false
        # -----------------------------
        exp3: Expressao = ExpAnd(
            ValorBooleano(True),
            ValorBooleano(False),
        )
        obtido = Exemplos.executar(exp3)
        resultados.append(
            {
                "caso": "3) true and false",
                "esperado": "false",
                "obtido": obtido,
                "ok": obtido == "false",
            }
        )

        # -----------------------------
        # 4) "Carreta" ++ " furacao " ++ " do brega"
        # -----------------------------
        exp4: Expressao = ExpConcat(
            ExpConcat(
                ValorString("Carreta"),
                ValorString(" furacao "),
            ),
            ValorString("do brega"),
        )
        obtido = Exemplos.executar(exp4)
        resultados.append(
            {
                "caso": '4) "Carreta" ++ " furacao " ++ "do brega"',
                "esperado": "Carreta furacao do brega",
                "obtido": obtido,
                "ok": obtido == "Carreta furacao do brega",
            }
        )

        # -----------------------------
        # 5) 1 + true  (ERRO DE TIPO)
        # -----------------------------
        exp5: Expressao = ExpSoma(
            ValorInteiro(1),
            ValorBooleano(True),
        )
        obtido = Exemplos.executar(exp5)
        resultados.append(
            {
                "caso": "5) 1 + true (ERRO DE TIPO)",
                "esperado": "Erro de tipo",
                "obtido": obtido,
                "ok": obtido == "Erro de tipo",
            }
        )

        # Exemplos extras que estavam aqui para cobrir todos os operadores
        # foram comentados/removidos a pedido, mantendo apenas as cinco
        # expressões transcritas do Java.

        return resultados


if __name__ == "__main__":
    for resultado in Exemplos.executar_todos():
        status = "OK" if resultado["ok"] else "FALHOU"
        print(f"[{status}] {resultado['caso']} -> {resultado['obtido']}")
