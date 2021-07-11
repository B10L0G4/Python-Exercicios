horario = int(input("Que horas são ?"))
#/testando a condição uma unica vez com o if:

if 0 < horario < 6:
    print("Ainda é de madrugada")
else:
    print("não é de madrugada")

#testando a condição em loop com while:

while 0 < horario < 6:
    print("Está de madrugada")#ira devolver o mesmo numero de horas
    horario += horario
else:
    print("não é madrugada")#quando o loop chegar ao fim será devolvido também


