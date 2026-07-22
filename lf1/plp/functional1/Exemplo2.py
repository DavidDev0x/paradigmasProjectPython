from __future__ import annotations

from pathlib import Path
import sys

# Permite executar este arquivo diretamente pela IDE, mesmo estando dentro do pacote.
_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from lf1.plp.expressions2.expression.exp_soma import ExpSoma
from lf1.plp.expressions2.expression.exp_sub import ExpSub
from lf1.plp.expressions2.expression.exp_equals import ExpEquals
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.expressions2.expression.valor_inteiro import ValorInteiro
from lf1.plp.expressions2.expression.valor_string import ValorString
from lf1.plp.functional1.programa import Programa
from lf1.plp.functional1.declaration.dec_funcao import DecFuncao
from lf1.plp.functional1.declaration.dec_variavel import DecVariavel
from lf1.plp.functional1.expression.aplicacao import Aplicacao
from lf1.plp.functional1.expression.exp_declaracao import ExpDeclaracao
from lf1.plp.functional1.expression.if_then_else import IfThenElse
from lf1.plp.functional1.util.valor_funcao import ValorFuncao


class Exemplo2:
    @staticmethod
    def criar_programa() -> Programa:
        funcao_f = ValorFuncao([Id("y")], ExpSoma(Id("y"), Id("x")))
        bloco_x5 = ExpDeclaracao(
            [DecVariavel(Id("x"), ValorInteiro(5))],
            Aplicacao(Id("f"), [ValorInteiro(1)]),
        )
        bloco_f = ExpDeclaracao([DecFuncao(Id("f"), funcao_f)], bloco_x5)
        bloco_x3 = ExpDeclaracao([DecVariavel(Id("x"), ValorInteiro(3))], bloco_f)
        return Programa(bloco_x3)

    @staticmethod
    def main() -> None:
        p = Exemplo2.criar_programa()
        print("Expressão : let var x=3 in let fun f y=y+x in let var x=5 in f(1)")
        print(f"Resultado : {p.executar()}")


if __name__ == "__main__":
    Exemplo2.main()
