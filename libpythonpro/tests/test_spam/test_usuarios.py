from libpythonpro.spam.usuario import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Luciano')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Luciano'), Usuario(nome='Cunha')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()




