horario = input('Digite o horário atual (hh:mm): ')

hora = horario[0:2]
minuto = horario[3:5]
#print(hora, minuto)
try:
    hora = int(hora)
    minuto = int(minuto)
    if hora>=0 and hora <11:
        print(f'Bom dia! São {hora} horas e {minuto} minutos.')
    elif hora>=11 and hora <17:
        print(f'Boa tarde! São {hora} horas e {minuto} minutos.')
    elif hora>=17 and hora <24:
        print(f'Boa noite! São {hora} horas e {minuto} minutos.')
    else:
        print('Provável que estejas fora do planeta Terra, pois o seu dia não possui 24 horas')
except:
    print('Horário informado no formato errado!')