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
    tipo_valido, resultado = Exemplo1.executar()
    print(f"Tipo valido: {tipo_valido}")
    print(f"Resultado: {resultado}")
