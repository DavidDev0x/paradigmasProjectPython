from le2.plp.expressions2.programa import Programa
from le2.plp.expressions2.declaration.dec_variavel import DecVariavel
from le2.plp.expressions2.expression import ExpDeclaracao, ExpSoma, Id, ValorInteiro


class Exemplo5:
    @staticmethod
    def criar_programa() -> Programa:
        dec_y = DecVariavel(Id("y"), Id("x"))
        corpo_mais_interno = ExpSoma(Id("x"), Id("y"))
        let_y = ExpDeclaracao([dec_y], corpo_mais_interno)

        dec_x_4 = DecVariavel(Id("x"), ExpSoma(Id("x"), ValorInteiro(1)))
        let_x_4 = ExpDeclaracao([dec_x_4], let_y)

        dec_x_3 = DecVariavel(Id("x"), ValorInteiro(3))
        let_x_3 = ExpDeclaracao([dec_x_3], let_x_4)
        return Programa(let_x_3)

    @staticmethod
    def executar() -> tuple[bool, str]:
        programa = Exemplo5.criar_programa()
        return programa.checa_tipo(), str(programa.executar())


if __name__ == "__main__":
    tipo_valido, resultado = Exemplo5.executar()
    print(f"Tipo valido: {tipo_valido}")
    print(f"Resultado: {resultado}")
