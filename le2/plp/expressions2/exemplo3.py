from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    project_root = Path(__file__).resolve().parents[3]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from le2.plp.expressions2.programa import Programa
from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression import ExpDeclaracao, ExpSoma, Id, ValorInteiro


class Exemplo3:
    @staticmethod
    def criar_programa() -> Programa:
        dec_x_2 = DecVariavel(Id("x"), ValorInteiro(2))
        corpo_mais_interno = ExpSoma(Id("x"), Id("y"))
        let_x_2 = ExpDeclaracao([dec_x_2], corpo_mais_interno)

        dec_y = DecVariavel(Id("y"), ExpSoma(Id("x"), ValorInteiro(1)))
        let_y = ExpDeclaracao([dec_y], let_x_2)

        dec_x_3 = DecVariavel(Id("x"), ValorInteiro(3))
        let_x_3 = ExpDeclaracao([dec_x_3], let_y)
        return Programa(let_x_3)

    @staticmethod
    def executar() -> tuple[bool, str]:
        programa = Exemplo3.criar_programa()
        return programa.checa_tipo(), str(programa.executar())


if __name__ == "__main__":
    programa = Exemplo3.criar_programa()
    print(f"Expressao: {programa.get_expressao()}")
    print(f"Tipo valido: {programa.checa_tipo()}")
    print(f"Resultado: {programa.executar()}")
