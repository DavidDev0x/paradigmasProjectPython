from __future__ import annotations

from typing import Any

from lf1.plp.expressions1.util.tipo import Tipo
from lf1.plp.expressions2.memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException
from lf1.plp.expressions2.memory.variavel_nao_declarada_exception import VariavelNaoDeclaradaException


class RestrictTypesVisitor:
    """Visitante de restrição de tipos portado do Java.

    A implementação evita importações diretas das classes de AST para reduzir
    acoplamento circular; o despacho usa o nome da classe e getters da própria AST.
    """

    def __init__(self) -> None:
        raise TypeError("RestrictTypesVisitor é uma classe utilitária.")

    @staticmethod
    def visit(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        nome = expressao.__class__.__name__
        if nome == "Aplicacao":
            return RestrictTypesVisitor._visit_aplicacao(expressao, ambiente, tipos, tipo_esperado)
        if nome == "ExpAnd":
            return RestrictTypesVisitor._visit_exp_and(expressao, ambiente, tipos, tipo_esperado)
        if nome == "ExpConcat":
            return RestrictTypesVisitor._visit_exp_concat(expressao, ambiente, tipos, tipo_esperado)
        if nome == "ExpDeclaracao":
            if hasattr(expressao, "get_seqdec_funcional"):
                return RestrictTypesVisitor._visit_exp_declaracao_funcional(expressao, ambiente, tipos, tipo_esperado)
            return RestrictTypesVisitor._visit_exp_declaracao(expressao, ambiente, tipos, tipo_esperado)
        if nome == "ExpEquals":
            return tipos
        if nome == "ExpLength":
            return RestrictTypesVisitor.visit(expressao.get_exp(), ambiente, tipos, Tipo.TIPO_STRING)
        if nome == "ExpMenos":
            return RestrictTypesVisitor.visit(expressao.get_exp(), ambiente, tipos, Tipo.TIPO_INTEIRO)
        if nome == "ExpNot":
            return RestrictTypesVisitor.visit(expressao.get_exp(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
        if nome == "ExpOr":
            return RestrictTypesVisitor._visit_exp_or(expressao, ambiente, tipos, tipo_esperado)
        if nome == "ExpSoma":
            return RestrictTypesVisitor._visit_exp_soma(expressao, ambiente, tipos, tipo_esperado)
        if nome == "ExpSub":
            return RestrictTypesVisitor._visit_exp_sub(expressao, ambiente, tipos, tipo_esperado)
        if nome == "IfThenElse":
            return RestrictTypesVisitor._visit_if_then_else(expressao, ambiente, tipos, tipo_esperado)
        if nome == "Id":
            return RestrictTypesVisitor._visit_id(expressao, ambiente, tipos, tipo_esperado)
        return tipos

    @staticmethod
    def _visit_aplicacao(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        try:
            tipo_funcao = ambiente.get(expressao.get_func())
        except Exception:
            tipo_funcao = tipos.get(expressao.get_func(), Tipo())
        tipo_atual = tipo_funcao
        aux = tipos
        for arg in expressao.get_args_expressao():
            if tipo_atual is None:
                break
            aux = RestrictTypesVisitor.visit(arg, ambiente, aux, tipo_atual)
            tipo_atual = tipo_atual.get_prox()
        return aux

    @staticmethod
    def _visit_exp_and(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        aux = RestrictTypesVisitor.visit(expressao.get_esq(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
        return RestrictTypesVisitor.visit(expressao.get_dir(), ambiente, aux, Tipo.TIPO_BOOLEANO)

    @staticmethod
    def _visit_exp_concat(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        aux = RestrictTypesVisitor.visit(expressao.get_esq(), ambiente, tipos, Tipo.TIPO_STRING)
        return RestrictTypesVisitor.visit(expressao.get_dir(), ambiente, aux, Tipo.TIPO_STRING)

    @staticmethod
    def _visit_exp_declaracao(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        ambiente.incrementa()
        try:
            for dec in expressao.get_seqdec_variavel():
                tipo_dec = dec.get_expressao().get_tipo(ambiente)
                ambiente.map(dec.get_id(), tipo_dec)
                tipos = RestrictTypesVisitor.visit(dec.get_expressao(), ambiente, tipos, tipo_dec)
            return RestrictTypesVisitor.visit(expressao.get_expressao(), ambiente, tipos, tipo_esperado)
        finally:
            ambiente.restaura()

    @staticmethod
    def _visit_exp_declaracao_funcional(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        ambiente.incrementa()
        try:
            for dec in expressao.get_seqdec_funcional():
                try:
                    if dec.get_aridade() == 0:
                        tipo_procurado = dec.get_expressao().get_tipo(ambiente)
                        ambiente.map(dec.get_id(), tipo_procurado)
                    else:
                        tipo_procurado = dec.get_funcao().get_tipo(ambiente)
                        if tipo_procurado != Tipo.TIPO_INDEFINIDO:
                            ambiente.map(dec.get_id(), tipo_procurado)
                except (VariavelJaDeclaradaException, VariavelNaoDeclaradaException):
                    tipo_procurado = Tipo()
                tipos = RestrictTypesVisitor.visit(dec.get_expressao(), ambiente, tipos, tipo_procurado)
            return RestrictTypesVisitor.visit(expressao.get_expressao(), ambiente, tipos, tipo_esperado)
        finally:
            ambiente.restaura()

    @staticmethod
    def _visit_exp_or(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        aux = RestrictTypesVisitor.visit(expressao.get_esq(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
        return RestrictTypesVisitor.visit(expressao.get_dir(), ambiente, aux, Tipo.TIPO_BOOLEANO)

    @staticmethod
    def _visit_exp_soma(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        aux = RestrictTypesVisitor.visit(expressao.get_esq(), ambiente, tipos, Tipo.TIPO_INTEIRO)
        return RestrictTypesVisitor.visit(expressao.get_dir(), ambiente, aux, Tipo.TIPO_INTEIRO)

    @staticmethod
    def _visit_exp_sub(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        aux = RestrictTypesVisitor.visit(expressao.get_esq(), ambiente, tipos, Tipo.TIPO_INTEIRO)
        return RestrictTypesVisitor.visit(expressao.get_dir(), ambiente, aux, Tipo.TIPO_INTEIRO)

    @staticmethod
    def _visit_if_then_else(expressao: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        aux = RestrictTypesVisitor.visit(expressao.get_condicao(), ambiente, tipos, Tipo.TIPO_BOOLEANO)
        aux = RestrictTypesVisitor.visit(expressao.get_then(), ambiente, aux, tipo_esperado)
        return RestrictTypesVisitor.visit(expressao.get_else_expressao(), ambiente, aux, tipo_esperado)

    @staticmethod
    def _visit_id(this_id: Any, ambiente: Any, tipos: dict[Any, Tipo], tipo_esperado: Tipo) -> dict[Any, Tipo]:
        for id_arg, tipo_atual in list(tipos.items()):
            if id_arg == this_id:
                tipos[id_arg] = tipo_esperado.intersecao(tipo_atual)
        return tipos
