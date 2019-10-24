#juan gines ramis vivancos p6ej3
print('introduce la primera nota')
nota=float(input())
notas=[]
notas.append(nota)
while 0<=nota<=10:
    print('introduce otra nota')
    nota=float(input())
    notas.append(nota)
notas.remove(nota)
print(notas)

