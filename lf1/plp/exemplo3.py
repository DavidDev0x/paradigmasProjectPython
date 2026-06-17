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


class Exemplo3:
    @staticmethod
    def criar_programa() -> Programa:
        funcao_f = ValorFuncao([Id("x")], ExpSoma(Id("x"), Id("y")))
        bloco_z = ExpDeclaracao(
            [DecVariavel(Id("z"), ValorString("abc"))],
            Aplicacao(Id("f"), [ValorInteiro(3)]),
        )
        bloco_f = ExpDeclaracao([DecFuncao(Id("f"), funcao_f)], bloco_z)
        bloco_y = ExpDeclaracao([DecVariavel(Id("y"), ValorInteiro(3))], bloco_f)
        return Programa(bloco_y)

    @staticmethod
    def main() -> None:
        p = Exemplo3.criar_programa()
        print('Expressão : let var y=3 in let fun f x=x+y in let var z="abc" in f(3)')
        print(f"Resultado : {p.executar()}")


if __name__ == "__main__":
    Exemplo3.main()
