from li1.plp.expressions2.expression import *
from li1.plp.imperative1.programa import Programa
from li1.plp.imperative1.command import *
from li1.plp.imperative1.declaration import *
from li1.plp.imperative1.memory import *

class Exemplo3:
    @staticmethod
    def criar_programa() -> Programa:
        i = Id('i')
        return Programa(ComandoDeclaracao(
            DeclaracaoVariavel(i, ValorInteiro(0)),
            While(ExpNot(ExpEquals(i, ValorInteiro(3))),
                  SequenciaComando(Atribuicao(i, ExpSoma(i, ValorInteiro(1))), Write(ValorString('Hello World'))))
        ))

    @staticmethod
    def main() -> str:
        programa = Exemplo3.criar_programa()
        if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
            return str(programa.executar(ContextoExecucaoImperativa(None)))
        return 'Erro de tipo: o programa Exemplo3 nao passou na checagem de tipos.'
