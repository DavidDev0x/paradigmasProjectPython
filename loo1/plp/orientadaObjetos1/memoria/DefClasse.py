class DefClasse:
    def __init__(self, id_classe, dec_variavel, dec_procedimento):
        self._id_classe = id_classe
        self._dec_variavel = dec_variavel
        self._dec_procedimento = dec_procedimento

    def get_dec_variavel(self):
        return self._dec_variavel

    def get_metodo(self, id_metodo):
        return self._dec_procedimento.get_procedimento(id_metodo)

    def get_tipo_atributo(self, id_atributo):
        return self._dec_variavel.get_tipo(id_atributo)

    def get_id_classe(self):
        return self._id_classe
