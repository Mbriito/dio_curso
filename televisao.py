class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 4

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminue_canal(self):
       if self.ligada:
        self.canal -= 1


    televisao = Televisao()              # instanciar
    print('Televisao esta ligda?: {}' .format(televisao.ligada))           # imprima televisao esta ligada
    televisao.power()                         # ligou a tv
    print('Televisao desligada: {}' .format(televisao.ligada))
    televisao.power()
    print(televisao.ligada)
    print('Canal: {}' .format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}' .format(televisao.canal))
    televisao.diminue_canal()
    televisao.diminue_canal()
    print('Canal: {}' .format(televisao.canal))



