def main ():
  largura = int(input("digite a largura"))
  altura = int(input("digite a altura"))
  
  if altura == 2:
     print (largura * "#")


  while altura >=1:
    print (largura * "#")
    if altura  >=3:
      print ( "#        #")
    altura -= 2


main ()
