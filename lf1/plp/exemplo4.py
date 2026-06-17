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


class Exemplo4:
    @staticmethod
    def dec_mult() -> DecFuncao:
        corpo_mult = IfThenElse(
            ExpEquals(Id("x"), ValorInteiro(0)),
            ValorInteiro(0),
            ExpSoma(
                Id("y"),
                Aplicacao(Id("mult"), [ExpSub(Id("x"), ValorInteiro(1)), Id("y")]),
            ),
        )
        return DecFuncao(Id("mult"), ValorFuncao([Id("x"), Id("y")], corpo_mult))

    @staticmethod
    def criar_programa_mult() -> Programa:
        programa_mult = ExpDeclaracao(
            [Exemplo4.dec_mult()],
            Aplicacao(Id("mult"), [ValorInteiro(3), ValorInteiro(4)]),
        )
        return Programa(programa_mult)

    @staticmethod
    def criar_programa_square() -> Programa:
        funcao_square = ValorFuncao(
            [Id("x")],
            Aplicacao(Id("mult"), [Id("x"), Id("x")]),
        )
        dec_square = DecFuncao(Id("square"), funcao_square)
        programa_square = ExpDeclaracao(
            [Exemplo4.dec_mult()],
            ExpDeclaracao([dec_square], Aplicacao(Id("square"), [ValorInteiro(7)])),
        )
        return Programa(programa_square)

    @staticmethod
    def main() -> None:
        p1 = Exemplo4.criar_programa_mult()
        print("Expressão : let fun mult x y = if x==0 then 0 else y+mult(x-1,y) in mult(3,4)")
        print(f"Resultado : {p1.executar()}")
        p2 = Exemplo4.criar_programa_square()
        print("Bônus — let fun mult... in let fun square x=mult(x,x) in square(7)")
        print(f"Resultado : {p2.executar()}")


if __name__ == "__main__":
    Exemplo4.main()
