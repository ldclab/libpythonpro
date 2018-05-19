from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.tests.test_spam.conftest import sessao


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador)
    enviador_de_spam.enviar_emails(
        'lucianodacunha.net@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
