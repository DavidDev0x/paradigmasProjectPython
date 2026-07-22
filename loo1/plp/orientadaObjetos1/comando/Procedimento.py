class Procedimento:
    def __init__(self, parametros_formais, comando):
        self._parametros_formais = parametros_formais
        self._comando = comando

    def get_parametros_formais(self):
        return self._parametros_formais

    def get_comando(self):
        return self._comando
