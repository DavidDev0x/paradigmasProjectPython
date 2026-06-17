from li1.plp.expressions2.expression import *
from li1.plp.imperative1.programa import Programa
from li1.plp.imperative1.command import *
from li1.plp.imperative1.declaration import *
from li1.plp.imperative1.memory import *

class Exemplo4:
    @staticmethod
    def criar_programa() -> Programa:
        n = Id('n')
        m = Id('n')
        return Programa(ComandoDeclaracao(
            DeclaracaoComposta(DeclaracaoVariavel(n, ValorInteiro(0)), DeclaracaoVariavel(m, ValorInteiro(0))),
            SequenciaComando(Atribuicao(n, ValorInteiro(2)), SequenciaComando(
                Atribuicao(m, ValorInteiro(3)),
                IfThenElse(ExpEquals(m, n), Write(ValorString('valores de entrada iguais')), Write(ValorString('valores de entrada diferentes')))
            ))
        ))

    @staticmethod
    def main() -> str:
        programa = Exemplo4.criar_programa()
        if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
            return str(programa.executar(ContextoExecucaoImperativa(None)))
        return 'Erro de tipo: o programa Exemplo4 nao passou na checagem de tipos.'
