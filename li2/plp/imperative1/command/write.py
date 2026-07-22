from li2.plp.imperative1.command.io import IO


class Write(IO):
    def __init__(self, expressao) -> None:
        self._expressao = expressao

    def executar(self, ambiente):
        ambiente.write(self._expressao.avaliar(ambiente))
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return self._expressao.checa_tipo(ambiente)
