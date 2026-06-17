from __future__ import annotations

from lf1.plp.exemplo1 import Exemplo1
from lf1.plp.exemplo2 import Exemplo2
from lf1.plp.exemplo3 import Exemplo3
from lf1.plp.exemplo4 import Exemplo4
from lf1.plp.expressions2.expression.exp_and import ExpAnd
from lf1.plp.expressions2.expression.exp_concat import ExpConcat
from lf1.plp.expressions2.expression.exp_equals import ExpEquals
from lf1.plp.expressions2.expression.exp_length import ExpLength
from lf1.plp.expressions2.expression.exp_menos import ExpMenos
from lf1.plp.expressions2.expression.exp_not import ExpNot
from lf1.plp.expressions2.expression.exp_or import ExpOr
from lf1.plp.expressions2.expression.exp_soma import ExpSoma
from lf1.plp.expressions2.expression.exp_sub import ExpSub
from lf1.plp.expressions2.expression.id import Id
from lf1.plp.expressions2.expression.valor_booleano import ValorBooleano
from lf1.plp.expressions2.expression.valor_inteiro import ValorInteiro
from lf1.plp.expressions2.expression.valor_string import ValorString
from lf1.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from lf1.plp.functional1.declaration.dec_variavel import DecVariavel
from lf1.plp.functional1.expression.exp_declaracao import ExpDeclaracao
from lf1.plp.functional1.programa import Programa


class Exemplos:
    @staticmethod
    def _executar_caso(nome: str, programa: Programa, esperado: str, resultados: list[str]) -> None:
        tipo_ok = programa.checa_tipo()
        valor = programa.executar()
        assert tipo_ok is True, f"{nome}: checa_tipo deveria ser True"
        assert str(valor) == esperado, f"{nome}: esperado {esperado}, obtido {valor}"
        resultados.append(f"OK - {nome}: {valor}")

    @staticmethod
    def _esperar_erro_tipo(nome: str, expressao, resultados: list[str]) -> None:
        programa = Programa(expressao)
        tipo_ok = programa.checa_tipo()
        assert tipo_ok is False, f"{nome}: checa_tipo deveria detectar erro"
        try:
            programa.executar()
        except TypeError as exc:
            resultados.append(f"OK - {nome}: erro de tipo capturado ({exc})")
            return
        raise AssertionError(f"{nome}: executar deveria lançar TypeError")

    @staticmethod
    def executar_todos() -> list[str]:
        resultados: list[str] = []

        Exemplos._executar_caso("Exemplo1 função simples f(2)", Exemplo1.criar_programa(), "3", resultados)
        Exemplos._executar_caso("Exemplo2 escopo dinâmico", Exemplo2.criar_programa(), "6", resultados)
        Exemplos._executar_caso("Exemplo3 função com variável externa", Exemplo3.criar_programa(), "6", resultados)
        Exemplos._executar_caso("Exemplo4 multiplicação recursiva", Exemplo4.criar_programa_mult(), "12", resultados)
        Exemplos._executar_caso("Exemplo4 bônus square", Exemplo4.criar_programa_square(), "49", resultados)

        operadores = [
            ("soma", Programa(ExpSoma(ValorInteiro(2), ValorInteiro(3))), "5"),
            ("subtração", Programa(ExpSub(ValorInteiro(7), ValorInteiro(2))), "5"),
            ("menos unário", Programa(ExpMenos(ValorInteiro(5))), "-5"),
            ("igualdade", Programa(ExpEquals(ValorInteiro(3), ValorInteiro(3))), "true"),
            ("and", Programa(ExpAnd(ValorBooleano(True), ValorBooleano(False))), "false"),
            ("or", Programa(ExpOr(ValorBooleano(True), ValorBooleano(False))), "true"),
            ("not", Programa(ExpNot(ValorBooleano(False))), "true"),
            ("concat", Programa(ExpConcat(ValorString("ab"), ValorString("cd"))), "abcd"),
            ("length", Programa(ExpLength(ValorString("abc"))), "3"),
        ]
        for nome, programa, esperado in operadores:
            Exemplos._executar_caso(f"operador {nome}", programa, esperado, resultados)

        Exemplos._esperar_erro_tipo("erro True + 2", ExpSoma(ValorBooleano(True), ValorInteiro(2)), resultados)
        Exemplos._esperar_erro_tipo("erro length(1)", ExpLength(ValorInteiro(1)), resultados)
        Exemplos._esperar_erro_tipo("erro string and boolean", ExpAnd(ValorString("x"), ValorBooleano(True)), resultados)

        duplicado = Programa(ExpDeclaracao([
            DecVariavel(Id("x"), ValorInteiro(1)),
            DecVariavel(Id("x"), ValorInteiro(2)),
        ], Id("x")))
        try:
            duplicado.checa_tipo()
        except VariavelJaDeclaradaException as exc:
            resultados.append(f"OK - declaração duplicada: {exc}")
        else:
            raise AssertionError("declaração duplicada deveria gerar VariavelJaDeclaradaException")

        for linha in resultados:
            print(linha)
        return resultados


if __name__ == "__main__":
    Exemplos.executar_todos()
