# FOR- laço de repetição especializado em navega entre objetos - 

nomes_cidades = ["São Paulo","Londres","Toquio","Paris"]
for nome in nomes_cidades:
    print(nome)

contador = 0
while contador <len(nomes_cidades):
    print(nomes_cidades[contador])
    contador += 1

    cidade = {
        "nome" : "São Paulo",
        "estado" : "São Paulo",
        "populção":12.2,
    } 
    for chave in cidade:
        print(f'{chave}:{cidade[chave]}')

    for nome in nomes_cidades:
        nome = "Rio de Janeiro"
        print(nomes_cidades)

for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = "Rio de JAneiro"
    print(nomes_cidades)


print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2 )))