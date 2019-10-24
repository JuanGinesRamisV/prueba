#juan gines ramis vivancos p5e4
print('dame un numero')
numero = int(input())
por = 1
for i in range(numero):
    por = por*(i+1)
    print(i)
print('El factorial de',numero, 'es',por,)
