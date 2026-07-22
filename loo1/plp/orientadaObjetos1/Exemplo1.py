# Permite executar este arquivo diretamente pela IDE ou pelo terminal.
if __name__ == "__main__" and __package__ in (None, ""):
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from loo1.plp.orientadaObjetos1.Programa import Programa
from loo1.plp.orientadaObjetos1.comando.Atribuicao import Atribuicao
from loo1.plp.orientadaObjetos1.comando.ChamadaMetodo import ChamadaMetodo
from loo1.plp.orientadaObjetos1.comando.ComDeclaracao import ComDeclaracao
from loo1.plp.orientadaObjetos1.comando.Sequencial import Sequencial
from loo1.plp.orientadaObjetos1.comando.Write import Write
from loo1.plp.orientadaObjetos1.declaracao.classe.DecClasseSimples import DecClasseSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoComposta import DecProcedimentoComposta
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoSimples import DecProcedimentoSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavelObjeto import DecVariavelObjeto
from loo1.plp.orientadaObjetos1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.plp.orientadaObjetos1.expressao.ListaExpressao import ListaExpressao
from loo1.plp.orientadaObjetos1.expressao.This import This
from loo1.plp.orientadaObjetos1.expressao.binaria.ExpSoma import ExpSoma
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributoThis import AcessoAtributoThis
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.memoria.ContextoCompilacaoOO1 import ContextoCompilacaoOO1
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo

class Exemplo1:
    @staticmethod
    def sequencial(*comandos):
        resultado = comandos[-1]
        for comando in reversed(comandos[:-1]):
            resultado = Sequencial(comando, resultado)
        return resultado

    @staticmethod
    def criar_programa() -> Programa:
        contador = Id("Contador")
        valor = Id("valor")
        imprimir = Id("print")
        inc = Id("inc")
        c = Id("c")

        this_valor = AcessoAtributoThis(This(), valor)
        atributos = SimplesDecVariavel(
            TipoPrimitivo.TIPO_INTEIRO, valor, ValorInteiro(1)
        )
        metodo_print = DecProcedimentoSimples(
            imprimir, ListaDeclaracaoParametro(), Write(this_valor)
        )
        metodo_inc = DecProcedimentoSimples(
            inc,
            ListaDeclaracaoParametro(),
            Atribuicao(this_valor, ExpSoma(this_valor, ValorInteiro(1))),
        )
        metodos = DecProcedimentoComposta(metodo_print, metodo_inc)
        declaracao_classe = DecClasseSimples(contador, atributos, metodos)
        declaracao_c = DecVariavelObjeto(TipoClasse(contador), c, contador)
        comando_principal = ComDeclaracao(
            declaracao_c,
            Exemplo1.sequencial(
                ChamadaMetodo(c, inc, ListaExpressao()),
                ChamadaMetodo(c, imprimir, ListaExpressao()),
            ),
        )
        return Programa(declaracao_classe, comando_principal)

    def executar(self):
        programa = self.criar_programa()
        if not programa.checa_tipo(ContextoCompilacaoOO1(ListaValor())):
            raise TypeError("O Exemplo1 não está bem tipado.")
        contexto = ContextoExecucaoOO1(ListaValor())
        contexto.get_ref()
        return programa.executar(contexto)


if __name__ == "__main__":
    exemplo = Exemplo1()
    exemplo.executar()
