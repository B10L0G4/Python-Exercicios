#numeros = (1,2,3,4,5) #usamos ao invés parenteses para tuplas 
numeros = 1,2,3,4,5,6 # pode ser declarada sem parenteses tambem 

# para acessar os valores usamos as mesmas 
#sintaxes das listas 

#mas as tuplas são imutaveis , nao é possivel
#alterar, modificar ou adicionar 

#podemos gerar uma tupla a partir de uma lista 

lista1 = [1,5,6,8,9,65]

tupla1 = tuple(lista1)

print(tupla1)

#ou uma lista a partir de uma tupla

tupla2 = [1,6,4,8] 
lista2 = list(tupla2)
print(lista2)

#tambel pode se usar o unpack

a, s, d, f, s, k = numeros
print("O primeiro vale", a,"o ultimo vale",k)

