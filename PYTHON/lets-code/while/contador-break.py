contador = 0
while True:
    if contador < 10:
        contador +=1
        if contador == 1:
            print(contador,"Item limpo")
        else:
            print(contador,"Itens Limpos")
    else:
        break
print("Fim")