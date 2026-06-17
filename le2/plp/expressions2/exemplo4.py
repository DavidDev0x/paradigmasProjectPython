from le2.plp.expressions2.programa import Programa
from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression import ExpDeclaracao, ExpSoma, Id, ValorInteiro


class Exemplo4:
    @staticmethod
    def criar_programa() -> Programa:
        dec_x_5 = DecVariavel(Id("x"), ValorInteiro(5))
        let_x_5 = ExpDeclaracao([dec_x_5], Id("y"))

        dec_y = DecVariavel(Id("y"), ExpSoma(Id("x"), ValorInteiro(1)))
        let_y = ExpDeclaracao([dec_y], let_x_5)

        dec_x_3 = DecVariavel(Id("x"), ValorInteiro(3))
        let_x_3 = ExpDeclaracao([dec_x_3], let_y)
        return Programa(let_x_3)

    @staticmethod
    def executar() -> tuple[bool, str]:
        programa = Exemplo4.criar_programa()
        return programa.checa_tipo(), str(programa.executar())


if __name__ == "__main__":
    tipo_valido, resultado = Exemplo4.executar()
    print(f"Tipo valido: {tipo_valido}")
    print(f"Resultado: {resultado}")
