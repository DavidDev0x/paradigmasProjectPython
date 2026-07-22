from .IO import IO


class Write(IO):
    def __init__(self, expressao):
        self._expressao = expressao

    def executar(self, ambiente):
        valor = self._expressao.avaliar(ambiente)
        print(valor)
        return ambiente.write(valor)

    def checa_tipo(self, ambiente) -> bool:
        return self._expressao.checa_tipo(ambiente)
