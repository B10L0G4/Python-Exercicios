animais = []
resposta = "s"

while resposta == "s" or resposta == "S":
    resposta = input("Deseja adicionar um animal? (s/n)")
    if (resposta == "s" or resposta == "S"):
        animal = input("Digite o nome animal ")
        animais.append(animal) #adicioando o nome do animal na lista
print(animais)
animal = input("digite o nome do animal a ser deletado")
animais.remove(animal)
print(animais)