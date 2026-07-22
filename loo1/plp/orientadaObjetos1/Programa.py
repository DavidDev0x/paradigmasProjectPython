from loo1.plp.orientadaObjetos1.excecao.execucao.EntradaNaoFornecidaException import EntradaNaoFornecidaException


class Programa:
    def __init__(self, dec_classe, comando):
        self._dec_classe = dec_classe
        self._comando = comando

    def executar(self, ambiente):
        if ambiente is None:
            raise EntradaNaoFornecidaException()
        self._dec_classe.elabora(ambiente)
        self._comando.executar(ambiente)
        return ambiente.get_saida()

    def checa_tipo(self, ambiente) -> bool:
        if ambiente is None:
            raise EntradaNaoFornecidaException()
        return self._dec_classe.checa_tipo(ambiente) and self._comando.checa_tipo(ambiente)
