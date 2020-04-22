class Enviador:
    def enviar(self, remitente, destinatario, asunto, cuerpo):
        if '@' not in remitente:
            raise EmailInvalido(f'Email del remitente inválido: {remitente}')
        return remitente


class EmailInvalido(Exception):
    pass
