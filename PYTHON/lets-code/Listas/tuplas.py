#assim como as listas podem ser definidas como uma sequencia ou coleçao de 
#valores ordenados, a diferença entre elas é a flexibilidade. 
#a tupla uma vez definida não pode ser alterada, é usada para 

nomes_paises = ("Brasil", "Argentina","China","Canada","Japao")
print(nomes_paises, type(nomes_paises))

print(len(nomes_paises))

nome_estados = "São Paulo", #a tupla não precisa de delimitadores 
#a tupla não tem sentido ser declarada vazia, mas pode ser feita uma 
#tupla com apenas 1 elemento 

#a tupla faz o unpack , diferente da lista que não executa essa função 
b, a, c, ca, j = nomes_paises

print(b,c,j)
print("O",j,"é uma pais asiatico")

#pode ser utilizada para parametros de funções 
print(*nomes_paises)




