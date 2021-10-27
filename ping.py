#Autor: Eduardo Chaparro

import ping3
ping3.EXCEPTIONS = True


def pingCheck():
    #identificacion de antenna
    print("ingrese antenna:", end="")
    prefijo = '10.192.'
    antenna = input()
    subfijo_ACU = '.21'

    #identificacion antenna
    if antenna>='41' and antenna<='65':
        prefijoAntenna = 'DA'

    print (prefijo+antenna+subfijo_ACU)
    #prueba de coneccion
    try:
        ping3.ping(prefijo+antenna+subfijo_ACU)
        print('ACU conectada')
    except ping3.errors.HostUnknown:
        print( "\033[1;31;42m"+"error direccion antenna")
    except ping3.errors.PingError:
        print('ACU '+prefijoAntenna+antenna+' sin conexion')

pingCheck()

