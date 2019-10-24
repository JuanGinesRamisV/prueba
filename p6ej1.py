#juan gines ramis vivancos
palabras=[]
print('introduce una palabra')
palabra=str(input())
palabras.append(palabra)
while palabra !='':
    print('introduce otra palabra')
    palabra=str(input())
    palabras.append(palabra)
palabras.remove('')
print(palabras)
