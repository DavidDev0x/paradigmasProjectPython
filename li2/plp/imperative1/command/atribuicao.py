from li2.plp.imperative1.command.comando import Comando


class Atribuicao(Comando):
    def __init__(self, identificador, expressao) -> None:
        self._id = identificador
        self._expressao = expressao

    def executar(self, ambiente):
        ambiente.change_valor(self._id, self._expressao.avaliar(ambiente))
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return self._expressao.checa_tipo(ambiente) and self._id.get_tipo(ambiente).e_igual(
            self._expressao.get_tipo(ambiente)
        )
