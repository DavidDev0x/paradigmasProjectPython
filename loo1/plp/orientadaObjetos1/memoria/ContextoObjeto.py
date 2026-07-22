class ContextoObjeto:
    def __init__(self, estado: dict):
        self._estado = dict(estado)

    def remove(self, identificador) -> None:
        self._estado.pop(identificador, None)

    def put(self, identificador, valor) -> None:
        self._estado[identificador] = valor

    def contains_key(self, identificador) -> bool:
        return identificador in self._estado

    def get(self, identificador):
        return self._estado.get(identificador)

    def as_dict(self) -> dict:
        return dict(self._estado)
