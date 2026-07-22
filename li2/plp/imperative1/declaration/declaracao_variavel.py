from li2.plp.imperative1.declaration.declaracao import Declaracao


class DeclaracaoVariavel(Declaracao):
    def __init__(self, identificador, expressao) -> None:
        self._id = identificador
        self._expressao = expressao

    def elabora(self, ambiente):
        ambiente.map(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def get_expressao(self):
        return self._expressao

    def get_id(self):
        return self._id

    def checa_tipo(self, ambiente) -> bool:
        resultado = self._expressao.checa_tipo(ambiente)
        if resultado:
            ambiente.map(self._id, self._expressao.get_tipo(ambiente))
        return resultado
