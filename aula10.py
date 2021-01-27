from datetime import date, time, datetime

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual) #data hora
    print(data_atual.strftime('%d:%m:%Y'))  #data
    print (data_atual.strftime('%d:%m:%Y - %H:%M:%S'))
    print (data_atual.strftime('%c')) # dia mes ano em formato brasileiro
    print(data_atual.day)
    print(data_atual.weekday())
    tuple = ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'Domingo')
    print(tuple[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A/%B/%Y')
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A/%B/%Y'))
    print(type(data_atual))
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_srt = horario.strftime('%H:%M:%S')
    print(type(horario_srt))
    print(type(horario))
    print(horario)



if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()