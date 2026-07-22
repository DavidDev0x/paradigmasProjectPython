from __future__ import annotations

import ast
import re

from li2.plp.expressions1.util.tipo_primitivo import TipoPrimitivo
from li2.plp.expressions2.expression.exp_and import ExpAnd
from li2.plp.expressions2.expression.exp_concat import ExpConcat
from li2.plp.expressions2.expression.exp_equals import ExpEquals
from li2.plp.expressions2.expression.exp_length import ExpLength
from li2.plp.expressions2.expression.exp_menos import ExpMenos
from li2.plp.expressions2.expression.exp_not import ExpNot
from li2.plp.expressions2.expression.exp_or import ExpOr
from li2.plp.expressions2.expression.exp_soma import ExpSoma
from li2.plp.expressions2.expression.exp_sub import ExpSub
from li2.plp.expressions2.expression.id import Id
from li2.plp.expressions2.expression.valor_booleano import ValorBooleano
from li2.plp.expressions2.expression.valor_inteiro import ValorInteiro
from li2.plp.expressions2.expression.valor_string import ValorString
from li2.plp.imperative1.command.atribuicao import Atribuicao
from li2.plp.imperative1.command.comando_declaracao import ComandoDeclaracao
from li2.plp.imperative1.command.if_then_else import IfThenElse
from li2.plp.imperative1.command.read import Read
from li2.plp.imperative1.command.sequencia_comando import SequenciaComando
from li2.plp.imperative1.command.skip import Skip
from li2.plp.imperative1.command.while_comando import While
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
from li2.plp.imperative2.parser.erro_sintatico import ErroSintatico
from li2.plp.imperative2.parser.token import Token


class Imp2Parser:
    _PALAVRAS = {
        "and": "AND", "or": "OR", "not": "NOT", "length": "LENGTH",
        "true": "TRUE", "false": "FALSE", "var": "VAR", "skip": "SKIP",
        "while": "WHILE", "do": "DO", "read": "READ", "write": "WRITE",
        "if": "IF", "then": "THEN", "else": "ELSE", "proc": "PROC",
        "call": "CALL", "int": "INT", "boolean": "BOOLEAN", "string": "STRING",
    }
    _TOKEN_RE = re.compile(
        r"(?P<WS>\s+)|"
        r"(?P<COMMENT>//[^\n\r]*(?:\r?\n|$)|/\*.*?\*/)|"
        r"(?P<STRING_LITERAL>\"(?:[^\"\\\n\r]|\\.)*\")|"
        r"(?P<INTEGER_LITERAL>0[xX][0-9a-fA-F]+|0[0-7]*|[1-9][0-9]*)|"
        r"(?P<OP>:=|==|\+\+|<=|>=|!=|\|\||&&|[=+\-*/%<>&|^~!?])|"
        r"(?P<SEP>[(){}\[\];,.])|"
        r"(?P<IDENTIFIER>[^\W\d]\w*)",
        re.DOTALL | re.UNICODE,
    )
    _SIMBOLOS = {
        ":=": "ATTRIB", "=": "ASSIGN", "==": "EQ", "++": "CONCAT",
        "+": "PLUS", "-": "MINUS", "(": "LPAREN", ")": "RPAREN",
        "{": "LBRACE", "}": "RBRACE", ";": "SEMICOLON", ",": "COMMA",
    }

    def __init__(self, fonte: str) -> None:
        self._tokens = self._tokenizar(fonte)
        self._indice = 0

    @classmethod
    def from_file(cls, caminho: str) -> "Imp2Parser":
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return cls(arquivo.read())

    def input(self) -> Programa:
        programa = Programa(self._parse_comando(set()))
        self._esperar("EOF")
        return programa

    def _tokenizar(self, fonte: str) -> list[Token]:
        tokens: list[Token] = []
        pos = 0
        while pos < len(fonte):
            match = self._TOKEN_RE.match(fonte, pos)
            if match is None:
                raise ErroSintatico(f"Símbolo inesperado na posição {pos}: {fonte[pos:pos+20]!r}")
            tipo = match.lastgroup
            texto = match.group()
            if tipo not in {"WS", "COMMENT"}:
                if tipo == "IDENTIFIER":
                    tipo = self._PALAVRAS.get(texto, "IDENTIFIER")
                elif tipo in {"OP", "SEP"}:
                    tipo = self._SIMBOLOS.get(texto, texto)
                tokens.append(Token(tipo, texto, pos))
            pos = match.end()
        tokens.append(Token("EOF", "", len(fonte)))
        return tokens

    def _atual(self) -> Token:
        return self._tokens[self._indice]

    def _aceitar(self, tipo: str) -> Token | None:
        if self._atual().tipo == tipo:
            token = self._atual()
            self._indice += 1
            return token
        return None

    def _esperar(self, tipo: str) -> Token:
        token = self._aceitar(tipo)
        if token is None:
            atual = self._atual()
            raise ErroSintatico(
                f"Esperado {tipo}, encontrado {atual.tipo} ({atual.texto!r}) na posição {atual.posicao}."
            )
        return token

    def _parse_comando(self, paradas: set[str]):
        comando = self._parse_comando_simples(paradas)
        if self._atual().tipo == "SEMICOLON" and "SEMICOLON" not in paradas:
            self._esperar("SEMICOLON")
            comando = SequenciaComando(comando, self._parse_comando(paradas))
        return comando

    def _parse_comando_simples(self, paradas: set[str]):
        tipo = self._atual().tipo
        if tipo == "SKIP":
            self._indice += 1
            return Skip()
        if tipo == "READ":
            self._indice += 1
            self._esperar("LPAREN")
            identificador = self._parse_id()
            self._esperar("RPAREN")
            return Read(identificador)
        if tipo == "WRITE":
            self._indice += 1
            self._esperar("LPAREN")
            expressao = self._parse_expressao()
            self._esperar("RPAREN")
            return Write(expressao)
        if tipo == "IF":
            self._indice += 1
            expressao = self._parse_expressao()
            self._esperar("THEN")
            comando_then = self._parse_comando({"ELSE"})
            self._esperar("ELSE")
            comando_else = self._parse_comando(paradas)
            return IfThenElse(expressao, comando_then, comando_else)
        if tipo == "WHILE":
            self._indice += 1
            expressao = self._parse_expressao()
            self._esperar("DO")
            return While(expressao, self._parse_comando(paradas))
        if tipo == "LBRACE":
            self._indice += 1
            declaracao = self._parse_declaracao()
            self._esperar("SEMICOLON")
            comando = self._parse_comando({"RBRACE"})
            self._esperar("RBRACE")
            return ComandoDeclaracao(declaracao, comando)
        if tipo == "CALL":
            self._indice += 1
            nome = self._parse_id()
            self._esperar("LPAREN")
            parametros = self._parse_lista_expressao()
            self._esperar("RPAREN")
            return ChamadaProcedimento(nome, parametros)
        if tipo == "LPAREN":
            self._indice += 1
            comando = self._parse_comando({"RPAREN"})
            self._esperar("RPAREN")
            return comando
        if tipo == "IDENTIFIER":
            identificador = self._parse_id()
            self._esperar("ATTRIB")
            return Atribuicao(identificador, self._parse_expressao())
        atual = self._atual()
        raise ErroSintatico(f"Comando inválido em {atual.posicao}: {atual.texto!r}")

    def _parse_declaracao(self):
        declaracao = self._parse_declaracao_simples()
        if self._aceitar("COMMA"):
            return DeclaracaoComposta(declaracao, self._parse_declaracao())
        return declaracao

    def _parse_declaracao_simples(self):
        if self._aceitar("VAR"):
            identificador = self._parse_id()
            self._esperar("ASSIGN")
            return DeclaracaoVariavel(identificador, self._parse_expressao())
        if self._aceitar("PROC"):
            nome = self._parse_id()
            self._esperar("LPAREN")
            parametros = self._parse_lista_declaracao_parametro()
            self._esperar("RPAREN")
            self._esperar("LBRACE")
            comando = self._parse_comando({"RBRACE"})
            self._esperar("RBRACE")
            return DeclaracaoProcedimento(nome, DefProcedimento(parametros, comando))
        atual = self._atual()
        raise ErroSintatico(f"Declaração inválida em {atual.posicao}: {atual.texto!r}")

    def _parse_lista_declaracao_parametro(self) -> ListaDeclaracaoParametro:
        itens = []
        if self._atual().tipo in {"INT", "BOOLEAN", "STRING"}:
            while True:
                tipo = self._parse_tipo()
                itens.append(DeclaracaoParametro(self._parse_id(), tipo))
                if not self._aceitar("COMMA"):
                    break
        resultado = ListaDeclaracaoParametro()
        for item in reversed(itens):
            resultado = ListaDeclaracaoParametro(item, resultado if resultado.get_head() is not None else None)
        return resultado

    def _parse_lista_expressao(self) -> ListaExpressao:
        itens = []
        if self._atual().tipo != "RPAREN":
            while True:
                itens.append(self._parse_expressao())
                if not self._aceitar("COMMA"):
                    break
        resultado = ListaExpressao()
        for item in reversed(itens):
            resultado = ListaExpressao(item, resultado)
        return resultado

    def _parse_tipo(self):
        if self._aceitar("INT"):
            return TipoPrimitivo.INTEIRO
        if self._aceitar("BOOLEAN"):
            return TipoPrimitivo.BOOLEANO
        if self._aceitar("STRING"):
            return TipoPrimitivo.STRING
        self._esperar("INT")

    def _parse_id(self) -> Id:
        return Id(self._esperar("IDENTIFIER").texto)

    def _parse_expressao(self):
        return self._parse_or()

    def _parse_or(self):
        expr = self._parse_and()
        while self._aceitar("OR"):
            expr = ExpOr(expr, self._parse_and())
        return expr

    def _parse_and(self):
        expr = self._parse_equals()
        while self._aceitar("AND"):
            expr = ExpAnd(expr, self._parse_equals())
        return expr

    def _parse_equals(self):
        expr = self._parse_concat()
        while self._aceitar("EQ"):
            expr = ExpEquals(expr, self._parse_concat())
        return expr

    def _parse_concat(self):
        expr = self._parse_aditiva()
        while self._aceitar("CONCAT"):
            expr = ExpConcat(expr, self._parse_aditiva())
        return expr

    def _parse_aditiva(self):
        expr = self._parse_unaria()
        while self._atual().tipo in {"PLUS", "MINUS"}:
            tipo = self._atual().tipo
            self._indice += 1
            direita = self._parse_unaria()
            expr = ExpSoma(expr, direita) if tipo == "PLUS" else ExpSub(expr, direita)
        return expr

    def _parse_unaria(self):
        if self._aceitar("MINUS"):
            return ExpMenos(self._parse_unaria())
        if self._aceitar("NOT"):
            return ExpNot(self._parse_unaria())
        if self._aceitar("LENGTH"):
            return ExpLength(self._parse_unaria())
        return self._parse_primaria()

    def _parse_primaria(self):
        token = self._atual()
        if self._aceitar("LPAREN"):
            expr = self._parse_expressao()
            self._esperar("RPAREN")
            return expr
        if token.tipo == "IDENTIFIER":
            return self._parse_id()
        if self._aceitar("TRUE"):
            return ValorBooleano(True)
        if self._aceitar("FALSE"):
            return ValorBooleano(False)
        if token.tipo == "INTEGER_LITERAL":
            self._indice += 1
            texto = token.texto
            base = 16 if texto.lower().startswith("0x") else (8 if len(texto) > 1 and texto.startswith("0") else 10)
            return ValorInteiro(int(texto, base))
        if token.tipo == "STRING_LITERAL":
            self._indice += 1
            return ValorString(ast.literal_eval(token.texto))
        raise ErroSintatico(f"Expressão inválida em {token.posicao}: {token.texto!r}")
