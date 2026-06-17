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


class Exemplo1:
    @staticmethod
    def criar_programa() -> Programa:
        funcao_f = ValorFuncao([Id("x")], ExpSoma(Id("x"), ValorInteiro(1)))
        dec_f = DecFuncao(Id("f"), funcao_f)
        chamada_f = Aplicacao(Id("f"), [ValorInteiro(2)])
        programa = ExpDeclaracao([dec_f], chamada_f)
        return Programa(programa)

    @staticmethod
    def main() -> None:
        p = Exemplo1.criar_programa()
        print("Expressão : let fun f x = x + 1 in f(2)")
        print(f"Resultado : {p.executar()}")


if __name__ == "__main__":
    Exemplo1.main()
