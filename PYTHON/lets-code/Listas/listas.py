# Criando uma lista vazia 
listavazia = []

#Criando uma lista com valores 
numero = [1,12,45,36,48,0]

#lista podem mesclar diferentes valores 
listamista = [1,2,3, "let's Code", 0.1, True]

#Acessando cada elemento da lista através de um indice entre colchetes
# Os índices começam em 0. 
print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
print(numero[4])

#Listas são mutaveis podemos alterar o valor de seus itens 
numero[2] = 5
print(numero)

#uma forma de trabalhar com listas usando loops

indice = 0
while indice < 5:
    print(numero[indice])
    indice += 1
    
