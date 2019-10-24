#p3e5
#Si el usuario introduce un número de más de tres cifras debe un informar con un mensaje de error como este “ ERROR: El número 1005 tiene más de tres cifras”.
print ('introduce un numero que no tenga mas de 3 digitos')
numero = float (input()) - 1000
if numero>=0:
    print('tu numero es incorrecto porque tiene mas de 3 cifras')
else:
    print('tu numero es valido')

