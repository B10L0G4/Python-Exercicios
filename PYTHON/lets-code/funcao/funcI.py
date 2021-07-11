def hello():
    print("Hello World")

hello() #chamada da função  

def calcula_media(valor1, valor2,valor3):
    soma = valor1 + valor2 + valor3
    media = soma/3
    return media

resultado = calcula_media(9, 10, 8)
print(resultado)

print("ola",end=" ")
print("Vans")

def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media 

resultado = calcula_media()
print(resultado)