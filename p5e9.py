#juan gines ramis vivancos p5e9
print('anchura del rectángulo')
copia=0
anchura = int(input())
print('altura del rectángulo')
altura = int(input())
copia = anchura
for i in range(altura):
    print('')
    if (i==0):
        print('*'*anchura)
    if (0<i<altura):
        print('*'+' '*(anchura-2)+'*')
    if (i+1==altura):
        print('*'*anchura)
            
