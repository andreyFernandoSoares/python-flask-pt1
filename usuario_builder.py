from usuario import Usuario

def constroi():
    usuario1 = Usuario('andy', 'Andrey Soares', '1234')
    usuario2 = Usuario('nico', 'Nico Steppat', '7a1')
    usuario3 = Usuario('flavio', 'Flavio Destiny', 'javascript')

    usuarios = {
        usuario1.id: usuario1,
        usuario2.id: usuario2,
        usuario3.id: usuario3
    }

    return usuarios