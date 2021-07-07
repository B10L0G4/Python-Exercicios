

nome_paises = ["Brasil","Argentina","China","Canadá","Japão"]
print("Tamanho da Lista", len(nome_paises))
print("País", nome_paises[4])
nome_paises[4] = "Colômbia"

print("País",nome_paises[4])
print(nome_paises)

print(nome_paises[1:3])# o indice final não é incluido no indice final 
print(nome_paises[1:-1])
print(nome_paises[2:])#omitir o indice final, significa que voce quer ir até o indice final da lista 
print(nome_paises[:3])#omiti o indice inicial  
print(nome_paises[:])#omite todos os valores , retorna a lista completa 
print(nome_paises[::2])#pula os itens da lista 
print(nome_paises[::-1])#inverte os itens de uma lista 
print("Brasil"in nome_paises)#verifica se um elemento esta contido na llista 
print("Canadá" not in nome_paises) #verifica se um elemento nao esta contido em uma lista 

lista_capitais = []

lista_capitais.append("São Paulo")#append insere elementos ao final da lista , apenas 1 por vez 
lista_capitais.append("Bogotá")
lista_capitais.append("Pequim")
lista_capitais.append("Buenos Aires")

print(lista_capitais)

lista_capitais.insert(2,"Paris")#insere um item em uma posição especifica
print(lista_capitais)

lista_capitais.remove("Buenos Aires")#deleta o item da lista 
print(lista_capitais)

lista_capitais.pop(2)#remove o elemento a partir da posção
#contudo ele sempre retorna o elemento removido , por isso ele deve 
# ser direcionado para uma variavél , afim de receber esse valor remnovido

removido = lista_capitais.pop(2)
print(lista_capitais, removido)



