class EntradaNaoFornecidaException(Exception):
    def __init__(self):
        super().__init__("Ambiente de execução ou compilação não fornecido.")
