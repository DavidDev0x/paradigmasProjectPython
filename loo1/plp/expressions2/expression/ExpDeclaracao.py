from .Expressao import Expressao
from loo1.plp.expressions2.memory.VariavelJaDeclaradaException import VariavelJaDeclaradaException


class ExpDeclaracao(Expressao):
    def __init__(self, declaracoes: list, expressao: Expressao):
        self._seqdec_variavel = list(declaracoes)
        self._expressao = expressao

    def _resolve_value_bindings(self, ambiente) -> dict:
        return {
            declaracao.get_id(): declaracao.get_expressao().avaliar(ambiente)
            for declaracao in self._seqdec_variavel
        }

    @staticmethod
    def _include_value_bindings(ambiente, resolvidos: dict) -> None:
        for identificador, valor in resolvidos.items():
            ambiente.map(identificador, valor)

    def avaliar(self, ambiente):
        ambiente.incrementa()
        try:
            resolvidos = self._resolve_value_bindings(ambiente)
            self._include_value_bindings(ambiente, resolvidos)
            return self._expressao.avaliar(ambiente)
        finally:
            ambiente.restaura()

    def _check_type_bindings(self, ambiente) -> bool:
        return all(d.get_expressao().checa_tipo(ambiente) for d in self._seqdec_variavel)

    def _resolve_type_bindings(self, ambiente) -> dict:
        resolvidos: dict = {}
        for declaracao in self._seqdec_variavel:
            identificador = declaracao.get_id()
            if identificador in resolvidos:
                raise VariavelJaDeclaradaException(identificador)
            resolvidos[identificador] = declaracao.get_expressao().get_tipo(ambiente)
        return resolvidos

    @staticmethod
    def _include_type_bindings(ambiente, resolvidos: dict) -> None:
        for identificador, tipo in resolvidos.items():
            ambiente.map(identificador, tipo)

    def checa_tipo(self, ambiente) -> bool:
        ambiente.incrementa()
        try:
            if not self._check_type_bindings(ambiente):
                return False
            resolvidos = self._resolve_type_bindings(ambiente)
            self._include_type_bindings(ambiente, resolvidos)
            return self._expressao.checa_tipo(ambiente)
        finally:
            ambiente.restaura()

    def get_tipo(self, ambiente):
        ambiente.incrementa()
        try:
            resolvidos = self._resolve_type_bindings(ambiente)
            self._include_type_bindings(ambiente, resolvidos)
            return self._expressao.get_tipo(ambiente)
        finally:
            ambiente.restaura()

    def reduzir(self, ambiente):
        ambiente.incrementa()
        try:
            for declaracao in self._seqdec_variavel:
                ambiente.map(declaracao.get_id(), None)
            self._expressao = self._expressao.reduzir(ambiente)
            return self
        finally:
            ambiente.restaura()

    def clone(self):
        from loo1.plp.expressions2.declaration.DecVariavel import DecVariavel
        novas = [
            DecVariavel(d.get_id().clone(), d.get_expressao().clone())
            for d in self._seqdec_variavel
        ]
        return ExpDeclaracao(novas, self._expressao.clone())
