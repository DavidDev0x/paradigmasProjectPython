from li2.plp.imperative1.command.comando import Comando


class Skip(Comando):
    def executar(self, ambiente):
        return ambiente

    def checa_tipo(self, ambiente) -> bool:
        return True
