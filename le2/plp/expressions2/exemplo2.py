from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    project_root = Path(__file__).resolve().parents[3]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from le2.plp.expressions2.programa import Programa
from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression import ExpDeclaracao, ExpSoma, Id, ValorInteiro


class Exemplo2:
    @staticmethod
    def criar_programa() -> Programa:
        dec_x_interno = DecVariavel(Id("x"), ValorInteiro(2))
        corpo_interno = ExpSoma(Id("x"), ValorInteiro(1))
        let_interno = ExpDeclaracao([dec_x_interno], corpo_interno)

        dec_x_externo = DecVariavel(Id("x"), ValorInteiro(1))
        let_externo = ExpDeclaracao([dec_x_externo], let_interno)
        return Programa(let_externo)

    @staticmethod
    def executar() -> tuple[bool, str]:
        programa = Exemplo2.criar_programa()
        return programa.checa_tipo(), str(programa.executar())


if __name__ == "__main__":
    programa = Exemplo2.criar_programa()
    print(f"Expressao: {programa.get_expressao()}")
    print(f"Tipo valido: {programa.checa_tipo()}")
    print(f"Resultado: {programa.executar()}")
