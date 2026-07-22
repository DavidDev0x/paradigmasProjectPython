from li2.plp.imperative1.command.io import IO
from li2.plp.imperative1.memory.erro_tipo_entrada_exception import ErroTipoEntradaException


class Read(IO):
    def __init__(self, identificador) -> None:
        self._id = identificador

    def executar(self, ambiente):
        valor_id = ambiente.get(self._id)
        valor_lido = ambiente.read()
        if valor_id.get_tipo(None).e_igual(valor_lido.get_tipo(None)):
            ambiente.change_valor(self._id, valor_lido)
            return ambiente
        raise ErroTipoEntradaException(
            f"Tipo do valor de entrada incompatível com o tipo da variável ({self._id.get_id_name()})"
        )

    def checa_tipo(self, ambiente) -> bool:
        ambiente.get(self._id)
        return True
