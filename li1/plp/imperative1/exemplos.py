from li1.plp.expressions2.expression import *
from li1.plp.imperative1.programa import Programa
from li1.plp.imperative1.command import *
from li1.plp.imperative1.declaration import *
from li1.plp.imperative1.memory import *

from li1.plp.expressions2.memory import VariavelJaDeclaradaException

class Exemplos:
    """Bateria de exemplos válidos e inválidos para LI1."""

    def _amb_comp(self) -> ContextoCompilacaoImperativa:
        return ContextoCompilacaoImperativa(None)

    def _amb_exec(self) -> ContextoExecucaoImperativa:
        return ContextoExecucaoImperativa(None)

    def avaliar_expressao(self, nome: str, expr) -> str:
        amb_c = self._amb_comp()
        ok = expr.checa_tipo(amb_c)
        if not ok:
            raise TypeError(f'Expressão {nome} não passou na checagem de tipos.')
        return str(expr.avaliar(self._amb_exec()))

    def criar_programa_read(self) -> Programa:
        x = Id('x')
        return Programa(ComandoDeclaracao(DeclaracaoVariavel(x, ValorInteiro(0)), SequenciaComando(Read(x), Write(x))))

    def executar_todos(self) -> dict[str, str]:
        resultados: dict[str, str] = {}

        validas = {
            'soma': ExpSoma(ValorInteiro(2), ValorInteiro(3)),
            'subtracao': ExpSub(ValorInteiro(10), ValorInteiro(4)),
            'menos_unario': ExpMenos(ValorInteiro(7)),
            'and': ExpAnd(ValorBooleano(True), ValorBooleano(False)),
            'or': ExpOr(ValorBooleano(True), ValorBooleano(False)),
            'not': ExpNot(ValorBooleano(False)),
            'igualdade_int': ExpEquals(ValorInteiro(5), ValorInteiro(5)),
            'concat': ExpConcat(ValorString('LI'), ValorString('1')),
            'length': ExpLength(ValorString('abc')),
        }
        for nome, expr in validas.items():
            resultados[nome] = self.avaliar_expressao(nome, expr)

        # Programa com read/write e entrada correta.
        entrada = ListaValor(ValorInteiro(42))
        programa_read = self.criar_programa_read()
        if programa_read.checa_tipo(ContextoCompilacaoImperativa(entrada)):
            resultados['read_write'] = str(programa_read.executar(ContextoExecucaoImperativa(ListaValor(ValorInteiro(42)))))

        # Programa com while.
        from li1.plp.imperative1.exemplo3 import Exemplo3
        resultados['while'] = Exemplo3.main()

        # Programa com if/else.
        n = Id('n')
        m = Id('m')
        prog_if = Programa(ComandoDeclaracao(
            DeclaracaoComposta(DeclaracaoVariavel(n, ValorInteiro(2)), DeclaracaoVariavel(m, ValorInteiro(3))),
            IfThenElse(ExpEquals(n, m), Write(ValorString('iguais')), Write(ValorString('diferentes')))
        ))
        if prog_if.checa_tipo(ContextoCompilacaoImperativa(None)):
            resultados['if_else'] = str(prog_if.executar(ContextoExecucaoImperativa(None)))

        # Erros esperados: todos devem ser capturados.
        erros = {
            'erro_true_como_inteiro': lambda: ValorInteiro(True),
            'erro_soma_bool_int': lambda: ExpSoma(ValorBooleano(True), ValorInteiro(2)).checa_tipo(ContextoCompilacaoImperativa(None)),
            'erro_concat_string_int': lambda: ExpConcat(ValorString('a'), ValorInteiro(1)).checa_tipo(ContextoCompilacaoImperativa(None)),
            'erro_if_nao_booleano': lambda: IfThenElse(ValorInteiro(1), Write(ValorString('x')), Write(ValorString('y'))).checa_tipo(ContextoCompilacaoImperativa(None)),
            'erro_variavel_duplicada': lambda: __import__('li1.plp.imperative1.exemplo4', fromlist=['Exemplo4']).Exemplo4.criar_programa().checa_tipo(ContextoCompilacaoImperativa(None)),
        }
        for nome, acao in erros.items():
            try:
                valor = acao()
                if valor is False:
                    resultados[nome] = 'erro de tipo detectado por checa_tipo=False'
                else:
                    resultados[nome] = f'FALHA: erro não detectado ({valor})'
            except Exception as exc:
                resultados[nome] = f'erro detectado: {type(exc).__name__}: {exc}'

        return resultados

if __name__ == '__main__':
    for chave, valor in Exemplos().executar_todos().items():
        print(f'{chave}: {valor}')
