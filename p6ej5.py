#juan gines ramis vivancos p6ej5
print('introduce un numero')
numeros=[]
numero=int(input())
numeros.append(numero)
print('introduce un numero mayor que', numero)
numero=int(input())
numeros.append(numero)
while numeros[-2]<numeros[-1]:
    print('introduce un numero mayor que', numero)
    numero=int(input())
    numeros.append(numero)
print('tus numeros son:',end='')
del numeros[-1]
for i in range(len(numeros)):
    if i==(len(numeros)-1):
        print(numeros[i], end='')
    if i!=(len(numeros)-1):
        print(numeros[i], ',', end='')

    
