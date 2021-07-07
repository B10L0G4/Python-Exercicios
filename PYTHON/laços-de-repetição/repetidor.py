largura = int(input("largura"))
altura = int(input("altura"))

#while largura >= 0:
if largura == altura :
    print ( largura * "#")
    print ( altura * "#")
else:
    print(largura * "#")
    altura = largura - altura  
    print(altura * "#" ,"\n")
   # print(largura * "#", altura * "@",end = "" )

    #while altura >=0 :
     #   print(altura * "@")
      #  altura -= 1 
