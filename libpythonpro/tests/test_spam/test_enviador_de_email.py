import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['outro@email.com', 'email.ldclab@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'lucianodacunha.net@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido von Rossum aberta'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    [' ', 'email']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'lucianodacunha.net@gmail.com',
            'Cursos Python Pro',
            'Primeira turma Guido von Rossum aberta'
        )
