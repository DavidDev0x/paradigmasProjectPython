# Permite executar este arquivo diretamente pela IDE.
if __package__ in (None, ""):
    import sys
    from pathlib import Path

    raiz_projeto = Path(__file__).resolve().parents[3]
    if str(raiz_projeto) not in sys.path:
        sys.path.insert(0, str(raiz_projeto))

from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression.exp_soma import ExpSoma
from li2.plp.expressions2.expression.id import Id
from li2.plp.expressions2.expression.valor_inteiro import ValorInteiro
from li2.plp.imperative1.command.atribuicao import Atribuicao
from li2.plp.imperative1.command.comando_declaracao import ComandoDeclaracao
from li2.plp.imperative1.command.sequencia_comando import SequenciaComando
from li2.plp.imperative1.command.write import Write
from li2.plp.imperative1.declaration.declaracao_composta import DeclaracaoComposta
from li2.plp.imperative1.declaration.declaracao_variavel import DeclaracaoVariavel
from li2.plp.imperative2.command.chamada_procedimento import ChamadaProcedimento
from li2.plp.imperative2.command.lista_expressao import ListaExpressao
from li2.plp.imperative2.declaration.declaracao_parametro import DeclaracaoParametro
from li2.plp.imperative2.declaration.declaracao_procedimento import DeclaracaoProcedimento
from li2.plp.imperative2.declaration.def_procedimento import DefProcedimento
from li2.plp.imperative2.declaration.lista_declaracao_parametro import ListaDeclaracaoParametro
from li2.plp.imperative2.programa import Programa
from li2.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from li2.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException
from li2.plp.imperative1.memory.contexto_compilacao_imperativa import ContextoCompilacaoImperativa
from li2.plp.imperative1.memory.entrada_vazia_exception import EntradaVaziaException
from li2.plp.imperative1.memory.erro_tipo_entrada_exception import ErroTipoEntradaException
from li2.plp.imperative1.memory.lista_valor import ListaValor
from li2.plp.imperative2.memory.contexto_execucao_imperativa2 import ContextoExecucaoImperativa2
from li2.plp.imperative2.memory.procedimento_ja_declarado_exception import ProcedimentoJaDeclaradoException
from li2.plp.imperative2.memory.procedimento_nao_declarado_exception import ProcedimentoNaoDeclaradoException


class Exemplo2:
    @staticmethod
    def criar_programa() -> Programa:
        x = Id("x")
        y = Id("y")
        p = Id("p")
        corpo_p = Atribuicao(x, ExpSoma(x, y))
        bloco_interno = ComandoDeclaracao(
            DeclaracaoVariavel(x, ValorInteiro(1)),
            SequenciaComando(
                ChamadaProcedimento(p, ListaExpressao(ValorInteiro(3))),
                Write(x),
            ),
        )
        return Programa(
            ComandoDeclaracao(
                DeclaracaoComposta(
                    DeclaracaoVariavel(x, ValorInteiro(0)),
                    DeclaracaoProcedimento(
                        p,
                        DefProcedimento(
                            ListaDeclaracaoParametro(
                                DeclaracaoParametro(y, TipoPrimitivo.INTEIRO)
                            ),
                            corpo_p,
                        ),
                    ),
                ),
                SequenciaComando(
                    bloco_interno,
                    SequenciaComando(
                        ChamadaProcedimento(p, ListaExpressao(ValorInteiro(4))),
                        Write(x),
                    ),
                ),
            )
        )

if __name__ == "__main__":
    exemplo = Exemplo2()
    programa = exemplo.criar_programa()

    try:
        bem_tipado = programa.checa_tipo(
            ContextoCompilacaoImperativa(ListaValor())
        )
        print(f"Programa bem tipado? {bem_tipado}")

        if bem_tipado:
            saida = programa.executar(
                ContextoExecucaoImperativa2(ListaValor())
            )
            print(f"Saida: {saida}")
    except ProcedimentoJaDeclaradoException as erro:
        print(f"Erro: procedimento ja declarado - {erro}")
    except ProcedimentoNaoDeclaradoException as erro:
        print(f"Erro: procedimento nao declarado - {erro}")
    except VariavelJaDeclaradaException as erro:
        print(f"Erro: variavel ja declarada - {erro}")
    except VariavelNaoDeclaradaException as erro:
        print(f"Erro: variavel nao declarada - {erro}")
    except EntradaVaziaException as erro:
        print(f"Erro: entrada vazia - {erro}")
    except ErroTipoEntradaException as erro:
        print(f"Erro: tipo de entrada invalido - {erro}")
