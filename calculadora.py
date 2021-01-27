class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
#print(calculadora.valor_a, valor_b)
print(calculadora.soma(2, 5))
print(calculadora.subtracao(3, 3))
print(calculadora.multiplicacao(6, 5))
print(calculadora.divisao(5, 10))