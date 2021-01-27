
from aula8_importacao import contador_letras
from calculadora import Calculadora

def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador


    if __name__ == '__main__':
        lista_palavras = contador_letras(lista)
        print("total letras po palavras de lista: {}" .format(total_letras))
        calculadora = Calculadora(5,19)
        print(calculadora.somA)

