from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    project_root = Path(__file__).resolve().parents[3]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from le2.plp.expressions2.programa import Programa
from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression import ExpDeclaracao, ExpSoma, Id, ValorInteiro


class Exemplo1:
    @staticmethod
    def criar_programa() -> Programa:
        x = Id("x")
        dec_x = DecVariavel(x, ValorInteiro(1))
        corpo = ExpSoma(Id("x"), ValorInteiro(1))
        exp = ExpDeclaracao([dec_x], corpo)
        return Programa(exp)

    @staticmethod
    def executar() -> tuple[bool, str]:
        programa = Exemplo1.criar_programa()
        return programa.checa_tipo(), str(programa.executar())


if __name__ == "__main__":
    programa = Exemplo1.criar_programa()
    print(f"Expressao: {programa.get_expressao()}")
    print(f"Tipo valido: {programa.checa_tipo()}")
    print(f"Resultado: {programa.executar()}")
