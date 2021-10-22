#Autor: Eduardo Chaparro
from requests import get, exceptions

def pingCheck():
    print("ingrese direccion:", end="")
    direccion = input()
    try:
        get("http://"+direccion, timeout=3)
        print('conectado')
    except exceptions.ConnectionError:
        print('no conectado')


pingCheck()


