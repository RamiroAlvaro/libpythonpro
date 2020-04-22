import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remitente',
    ['ramiroalvaro.ra@gmail.com', 'foo@bar.com.br'])
def test_remetente(remitente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remitente,
        'renzo@python.pro.br',
        'Cursos Python Pro',
        'Primera turma Guido Von Rossum abierta.'
    )
    assert remitente in resultado


@pytest.mark.parametrize(
    'remitente',
    ['ramiroalvaro.ra', ''])
def test_remetente_invalido(remitente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remitente,
            'renzo@python.pro.br',
            'Cursos Python Pro',
            'Primera turma Guido Von Rossum abierta.'
        )
