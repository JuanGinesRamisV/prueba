#juan gines ramis vivancos p6ej2
print('introduce un numero')
numero=int(input())
numeros=[]
numeros.append(numero)
while numero!=('salir'):
    print('introduce otro numero')
    numero=str(input())
    if numero!=('salir'):
       numeros.append(numero) 
print(numeros)
