from .IO import IO


class Read(IO):
    def __init__(self, identificador):
        self._id = identificador
        self._tipo_id = None

    def executar(self, ambiente):
        if self._tipo_id is None:
            raise RuntimeError("Execute checa_tipo antes de Read.executar.")
        ambiente.change_valor(self._id, ambiente.read(self._tipo_id))
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        self._tipo_id = self._id.get_tipo(ambiente)
        return self._id.checa_tipo(ambiente)
