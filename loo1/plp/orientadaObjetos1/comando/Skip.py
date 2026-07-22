from .Comando import Comando


class Skip(Comando):
    def executar(self, ambiente):
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return True
