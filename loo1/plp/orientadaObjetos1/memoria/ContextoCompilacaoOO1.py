from .AmbienteCompilacaoOO1 import AmbienteCompilacaoOO1
from loo1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException
from loo1.plp.expressions2.memory.VariavelNaoDeclaradaException import VariavelNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseJaDeclaradaException import ClasseJaDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ClasseNaoDeclaradaException import ClasseNaoDeclaradaException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoJaDeclaradoException import ProcedimentoJaDeclaradoException
from loo1.plp.orientadaObjetos1.excecao.declaracao.ProcedimentoNaoDeclaradoException import ProcedimentoNaoDeclaradoException


class ContextoCompilacaoOO1(AmbienteCompilacaoOO1):
    def __init__(self, entrada=None):
        self._pilha: list[dict] = []
        self._pilha_procedimento: list[dict] = []
        self._map_def_classe: dict = {}
        self._entrada = entrada

    def incrementa(self) -> None:
        self._pilha.append({})
        self._pilha_procedimento.append({})

    def restaura(self) -> None:
        if not self._pilha:
            raise RuntimeError("Não há escopo de compilação para restaurar.")
        self._pilha.pop()
        self._pilha_procedimento.pop()

    def map(self, identificador, tipo) -> None:
        if not self._pilha:
            raise RuntimeError("Crie um escopo antes de mapear tipos.")
        if identificador in self._pilha[-1]:
            raise VariavelJaDeclaradaException(identificador)
        self._pilha[-1][identificador] = tipo

    def map_parametros_procedimento(self, identificador, parametros) -> None:
        if not self._pilha_procedimento:
            raise RuntimeError("Crie um escopo antes de mapear procedimentos.")
        if identificador in self._pilha_procedimento[-1]:
            raise ProcedimentoJaDeclaradoException(identificador)
        self._pilha_procedimento[-1][identificador] = parametros

    def map_def_classe(self, identificador, definicao) -> None:
        if identificador in self._map_def_classe:
            raise ClasseJaDeclaradaException(identificador)
        self._map_def_classe[identificador] = definicao

    def get(self, identificador):
        for escopo in reversed(self._pilha):
            if identificador in escopo and escopo[identificador] is not None:
                return escopo[identificador]
        raise VariavelNaoDeclaradaException(identificador)

    def get_tipo(self, identificador):
        return self.get(identificador)

    def get_parametros_procedimento(self, identificador):
        for escopo in reversed(self._pilha_procedimento):
            if identificador in escopo and escopo[identificador] is not None:
                return escopo[identificador]
        raise ProcedimentoNaoDeclaradoException(identificador)

    def get_def_classe(self, identificador):
        if identificador not in self._map_def_classe:
            raise ClasseNaoDeclaradaException(identificador)
        return self._map_def_classe[identificador]

    def get_tipo_entrada(self):
        if self._entrada is None or self._entrada.length() == 0:
            raise VariavelNaoDeclaradaException("<entrada>")
        tipo = self._entrada.get_head().get_tipo(self)
        self._entrada = self._entrada.get_tail()
        return tipo
