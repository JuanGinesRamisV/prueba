#juan gines ramis vivancos p5e2
print('Escribe un número')
numero1 = int(input())
print('Escribe un numero mayor que' ,numero1,)
numero2 = int(input())
for i in range(numero1,numero2+1):
    if ((i%2) == 0):
        print(i, 'es par')
    else:
        print(i, 'es inpar')
    
