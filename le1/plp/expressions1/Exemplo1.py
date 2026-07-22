from __future__ import annotations

# Permite executar este arquivo diretamente na IDE sem instalar o pacote.
# Ex.: clicar em Run no PyCharm/VS Code ou usar: python le1/plp/expressions1/Exemplo1.py
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from le1.plp.expressions1 import Programa
from le1.plp.expressions1.expression import ExpSoma, ExpSub, Expressao, ValorInteiro


class Exemplo1:
    @staticmethod
    def main() -> None:
        e1: Expressao = ValorInteiro(3)
        e2: Expressao = ValorInteiro(12)
        e3: Expressao = ValorInteiro(3)
        soma: Expressao = ExpSoma(e1, e2)
        expressao_final: Expressao = ExpSub(soma, e3)
        programa = Programa(expressao_final)
        if programa.checa_tipo():
            programa.executar()
        else:
            print("Erro de tipo")


if __name__ == "__main__":
    Exemplo1.main()
