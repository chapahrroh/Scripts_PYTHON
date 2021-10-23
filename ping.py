#Autor: Eduardo Chaparro

from requests import get, exceptions

def pingCheck():
    print("ingrese direccion:", end="")
    direccion = input()
    try:
        get("http://"+direccion, timeout=3)
        print('conectado')
    except exceptions.ConnectionError:
        print( "\033[1;31;42m"+"no conectado")

pingCheck()

