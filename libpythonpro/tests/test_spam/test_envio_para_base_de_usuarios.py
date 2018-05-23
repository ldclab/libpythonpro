from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.usuario import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Luciano', email='luciano@email.com'),
            Usuario(nome='Cunha', email='cunha@email.com')
        ],
        [
            Usuario(nome='Cunha', email='cunha@email.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

    assert len(usuarios) == enviador.enviar.call_count

def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )


# class EnviadorMock(Enviador):
#     def __init__(self):
#         super().__init__()
#         self.qtd_email_enviados = 0
#         self.parametros_de_envio = None
#
#     def enviar(self, remetente, destinatario, assunto, corpo):
#         self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
#         self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Luciano', email='cunha@email.com')
    sessao.salvar(usuario)
    # enviador = EnviadorMock()
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@email.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )

    enviador.enviar.assert_called_once_with(
        'luciano@email.com',
        'cunha@email.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
