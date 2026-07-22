# Permite executar este arquivo diretamente pela IDE ou pelo terminal.
if __name__ == "__main__" and __package__ in (None, ""):
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from loo1.plp.orientadaObjetos1.Programa import Programa
from loo1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseJaDeclaradaException import ClasseJaDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoJaDeclaradoException import ObjetoJaDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ObjetoNaoDeclaradoException import ObjetoNaoDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoJaDeclaradoException import ProcedimentoJaDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.execucao.EntradaInvalidaException import EntradaInvalidaException
from loo1.plp.orientadaObjetos1.excecao.execucao.EntradaNaoFornecidaException import EntradaNaoFornecidaException
from loo1.plp.orientadaObjetos1.comando.Atribuicao import Atribuicao
from loo1.plp.orientadaObjetos1.comando.ChamadaMetodo import ChamadaMetodo
from loo1.plp.orientadaObjetos1.comando.ComDeclaracao import ComDeclaracao
from loo1.plp.orientadaObjetos1.comando.IfThenElse import IfThenElse
from loo1.plp.orientadaObjetos1.comando.New import New
from loo1.plp.orientadaObjetos1.comando.Sequencial import Sequencial
from loo1.plp.orientadaObjetos1.comando.Skip import Skip
from loo1.plp.orientadaObjetos1.comando.While import While
from loo1.plp.orientadaObjetos1.comando.Write import Write
from loo1.plp.orientadaObjetos1.declaracao.classe.DecClasseSimples import DecClasseSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecParametro import DecParametro
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoComposta import DecProcedimentoComposta
from loo1.plp.orientadaObjetos1.declaracao.procedimento.DecProcedimentoSimples import DecProcedimentoSimples
from loo1.plp.orientadaObjetos1.declaracao.procedimento.ListaDeclaracaoParametro import ListaDeclaracaoParametro
from loo1.plp.orientadaObjetos1.declaracao.variavel.CompostaDecVariavel import CompostaDecVariavel
from loo1.plp.orientadaObjetos1.declaracao.variavel.DecVariavelObjeto import DecVariavelObjeto
from loo1.plp.orientadaObjetos1.declaracao.variavel.SimplesDecVariavel import SimplesDecVariavel
from loo1.plp.orientadaObjetos1.expressao.ListaExpressao import ListaExpressao
from loo1.plp.orientadaObjetos1.expressao.This import This
from loo1.plp.orientadaObjetos1.expressao.binaria.ExpEquals import ExpEquals
from loo1.plp.orientadaObjetos1.expressao.binaria.ExpOr import ExpOr
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributoId import AcessoAtributoId
from loo1.plp.orientadaObjetos1.expressao.leftExpression.AcessoAtributoThis import AcessoAtributoThis
from loo1.plp.orientadaObjetos1.expressao.leftExpression.Id import Id
from loo1.plp.orientadaObjetos1.expressao.unaria.ExpNot import ExpNot
from loo1.plp.orientadaObjetos1.expressao.valor.ValorInteiro import ValorInteiro
from loo1.plp.orientadaObjetos1.expressao.valor.ValorNull import ValorNull
from loo1.plp.orientadaObjetos1.memoria.ContextoCompilacaoOO1 import ContextoCompilacaoOO1
from loo1.plp.orientadaObjetos1.memoria.ContextoExecucaoOO1 import ContextoExecucaoOO1
from loo1.plp.orientadaObjetos1.memoria.colecao.ListaValor import ListaValor
from loo1.plp.orientadaObjetos1.util.TipoClasse import TipoClasse
from loo1.plp.orientadaObjetos1.util.TipoPrimitivo import TipoPrimitivo


class Exemplo4:
    @staticmethod
    def sequencial(*comandos):
        resultado = comandos[-1]
        for comando in reversed(comandos[:-1]):
            resultado = Sequencial(comando, resultado)
        return resultado

    @staticmethod
    def criar_programa() -> Programa:
        l_valor = Id("LValor")
        valor = Id("valor")
        prox = Id("prox")
        insere = Id("insere")
        remove = Id("remove")
        imprimir = Id("print")
        v = Id("v")
        aux = Id("aux")
        lv = Id("lv")
        tipo_l_valor = TipoClasse(l_valor)

        this_valor = AcessoAtributoThis(This(), valor)
        this_prox = AcessoAtributoThis(This(), prox)
        atributos = CompostaDecVariavel(
            SimplesDecVariavel(
                TipoPrimitivo.TIPO_INTEIRO, valor, ValorInteiro(-100)
            ),
            SimplesDecVariavel(tipo_l_valor, prox, ValorNull()),
        )

        corpo_insere = IfThenElse(
            ExpEquals(this_valor, ValorInteiro(-100)),
            Exemplo4.sequencial(
                Atribuicao(this_valor, v),
                New(this_prox, l_valor),
            ),
            ChamadaMetodo(this_prox, insere, ListaExpressao(v)),
        )
        metodo_insere = DecProcedimentoSimples(
            insere,
            ListaDeclaracaoParametro(
                DecParametro(v, TipoPrimitivo.TIPO_INTEIRO)
            ),
            corpo_insere,
        )

        aux_prox = AcessoAtributoId(aux, prox)
        aux_prox_valor = AcessoAtributoId(aux_prox, valor)
        aux_prox_prox = AcessoAtributoId(aux_prox, prox)
        corpo_remove = ComDeclaracao(
            SimplesDecVariavel(tipo_l_valor, aux, This()),
            Exemplo4.sequencial(
                While(
                    ExpNot(
                        ExpOr(
                            ExpEquals(aux_prox, ValorNull()),
                            ExpEquals(aux_prox_valor, v),
                        )
                    ),
                    Atribuicao(aux, aux_prox),
                ),
                IfThenElse(
                    ExpNot(ExpEquals(aux_prox, ValorNull())),
                    Atribuicao(aux_prox, aux_prox_prox),
                    Skip(),
                ),
            ),
        )
        metodo_remove = DecProcedimentoSimples(
            remove,
            ListaDeclaracaoParametro(
                DecParametro(v, TipoPrimitivo.TIPO_INTEIRO)
            ),
            corpo_remove,
        )

        corpo_print = Exemplo4.sequencial(
            Write(this_valor),
            IfThenElse(
                ExpNot(ExpEquals(this_prox, ValorNull())),
                ChamadaMetodo(this_prox, imprimir, ListaExpressao()),
                Skip(),
            ),
        )
        metodo_print = DecProcedimentoSimples(
            imprimir, ListaDeclaracaoParametro(), corpo_print
        )
        metodos = DecProcedimentoComposta(
            metodo_insere,
            DecProcedimentoComposta(metodo_remove, metodo_print),
        )
        declaracao_classe = DecClasseSimples(l_valor, atributos, metodos)
        declaracao_lv = DecVariavelObjeto(tipo_l_valor, lv, l_valor)
        comando_principal = ComDeclaracao(
            declaracao_lv,
            Exemplo4.sequencial(
                ChamadaMetodo(lv, insere, ListaExpressao(ValorInteiro(2))),
                ChamadaMetodo(lv, insere, ListaExpressao(ValorInteiro(3))),
                ChamadaMetodo(lv, insere, ListaExpressao(ValorInteiro(4))),
                ChamadaMetodo(lv, imprimir, ListaExpressao()),
                ChamadaMetodo(lv, remove, ListaExpressao(ValorInteiro(3))),
                ChamadaMetodo(lv, imprimir, ListaExpressao()),
            ),
        )
        return Programa(declaracao_classe, comando_principal)

    @staticmethod
    def tratar(tipo: str, erro: Exception) -> None:
        import sys

        print(f"{tipo}: {erro}", file=sys.stderr)

    def executar(self):
        programa = self.criar_programa()

        try:
            bem_tipado = programa.checa_tipo(
                ContextoCompilacaoOO1(ListaValor())
            )

            if bem_tipado:
                contexto = ContextoExecucaoOO1(ListaValor())
                contexto.get_ref()
                return programa.executar(contexto)
        except VariavelNaoDeclaradaException as erro:
            self.tratar("VariavelNaoDeclaradaException", erro)
        except VariavelJaDeclaradaException as erro:
            self.tratar("VariavelJaDeclaradaException", erro)
        except ObjetoNaoDeclaradoException as erro:
            self.tratar("ObjetoNaoDeclaradoException", erro)
        except ObjetoJaDeclaradoException as erro:
            self.tratar("ObjetoJaDeclaradoException", erro)
        except ProcedimentoNaoDeclaradoException as erro:
            self.tratar("ProcedimentoNaoDeclaradoException", erro)
        except ProcedimentoJaDeclaradoException as erro:
            self.tratar("ProcedimentoJaDeclaradoException", erro)
        except ClasseNaoDeclaradaException as erro:
            self.tratar("ClasseNaoDeclaradaException", erro)
        except ClasseJaDeclaradaException as erro:
            self.tratar("ClasseJaDeclaradaException", erro)
        except EntradaNaoFornecidaException as erro:
            self.tratar("EntradaNaoFornecidaException", erro)
        except EntradaInvalidaException as erro:
            self.tratar("EntradaInvalidaException", erro)

if __name__ == "__main__":
    exemplo = Exemplo4()
    exemplo.executar()
