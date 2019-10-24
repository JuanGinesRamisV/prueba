#juan gines rammis vivvancos p4e4

print('introduce 3 numeros')
n1 = int(input())
n2 = int(input())
n3 = int(input())
print('introduce un numero y comprobare si es divisor de los 3 primeros')
n4 = int(input())
if n1%n4 == 0:
    print(n1, 'es divisor de' ,n4,)
    if (n2%n4 == 0):
        print(n2, 'es divisor de' ,n4,)
        if(n3%n4 == 0):
            print(n3, 'es divisor de' ,n4,)
        else: print(n3 ,'no es divisor de' ,n4,)
    else:
        print(n2, 'no es divisor de' ,n4,)
        if (n3%n4 == 0):
            print(n3, 'es divisor de' ,n4,)
        else:
            print(n3, 'no es divisor de' ,n4,)

else:
    print('el numero' ,n1, ' no es divisor de' ,n4,)
    if (n2%n4 == 0):
        print(n2, 'es divisor de' ,n4,)
        if(n3%n4 == 0):
            print(n3, 'es divisor de' ,n4,)
        else: print(n3 ,'no es divisor de' ,n4,)
    else: print(n3, 'no es divisor de' ,n4,)
