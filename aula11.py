class Error(Exception):
    pass


class inputError(Error):
    def __init__(self, message): 
        self.message = message 


while True:
    try:
        x = int(input('Ebtre com a nota de ) a 10: '))
        print(x)
        if x > 10:    #forçar uma eccesao com comando raise
            raise inputError('1nota nao pode ser maior que 10.') #imputerro é uma classe e o paramentro e a messagem
        elif x < 0:
            raise inputError('nota nao pode ser menor que zero')
        break
    except ValueError:
        print('valor invalido.Devse digitar apenas numeros.')   
    except inputError as ex:
        print(ex)     


lista = [1, 10]

"""
try:   #tratemento de exceção
    divisao = 10 / 0
    numero = lista[1]
except Exception as ex:
    print('erro desconhecido. Erro: {}' .format(ex))  
except ZeroDivisionError:#classe de excesao
    print(' não é possivel realizar uma divisao por 0')

except IndexError: 
    print('erro ao acessar um indice invalido da lista')
else:
    print('executa quando nao ocorrer excecão')
"""

