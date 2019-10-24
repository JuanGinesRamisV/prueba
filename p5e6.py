#juan gines ramis vivancos p5e6
print('introduce la altura de tu trianuglo')
altura = int(input())
anchura = altura
for i in range(altura):
    print()
    anchura = altura-(1*i)
    for i in range(anchura):
        print('*', end='')
        
