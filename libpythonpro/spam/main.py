class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.enviador = enviador
        self.sessao = sessao

    def enviar_emails(self, remitente, asunto, cuerpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                remitente,
                usuario.email,
                asunto,
                cuerpo
            )
