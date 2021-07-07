def soma_elementos (soma):
    s = []
    for i in soma:
        if i not in s:
            s.append(i)
    s = sum(soma)
    return s 
soma = [1,2,3,3,6]
soma = soma_elementos(soma)
print (soma)
  
