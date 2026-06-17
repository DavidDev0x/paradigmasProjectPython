from li1.plp.expressions2.expression import *
from li1.plp.imperative1.programa import Programa
from li1.plp.imperative1.command import *
from li1.plp.imperative1.declaration import *
from li1.plp.imperative1.memory import *

class Exemplo1:
    @staticmethod
    def criar_programa() -> Programa:
        a = Id('3')
        return Programa(ComandoDeclaracao(DeclaracaoVariavel(a, ValorInteiro(3)), Write(a)))

    @staticmethod
    def main() -> str:
        programa = Exemplo1.criar_programa()
        if programa.checa_tipo(ContextoCompilacaoImperativa(None)):
            return str(programa.executar(ContextoExecucaoImperativa(None)))
        return 'Erro de tipo: o programa Exemplo1 nao passou na checagem de tipos.'
