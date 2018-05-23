from libpythonpro.spam.usuario import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Luciano', email='luciano@email.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Luciano', email='luciano@email.com'),
        Usuario(nome='Cunha', email='cunha@email.com')
    ]

    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()




