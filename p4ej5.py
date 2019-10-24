#juan gines ramis vivancos P4ej5
billete_500 = 500
billete_200 = 200
billete_100 = 100
billete_50 = 50
billete_20 = 20
billete_10 = 10
billete_5 = 5
print('introduce la cantidad que quieres sacar')
cantidad = int(input())
if cantidad%500 == 0:
    (billete) = cantidad/500
    print('te doy' ,billete, 'billetes de 500')
elif cantidad%200 == 0:
    billete = cantidad/200
    print('te doy' ,billete, 'billetes de 200')
elif cantidad%100 == 0:
    (billete) = cantidad/100
    print('te doy' ,billete, 'billetes de 100')
elif cantidad%50 == 0:
    (billete) = cantidad/50
    print('te doy' ,billete, 'billetes de 50')
elif cantidad%20 == 0:
    (billete) = cantidad/20
    print('te doy' ,billete, 'billetes de 20')
elif cantidad%10 == 0:
    (billete) = cantidad/10
    print('te doy' ,billete, 'billetes de 10')
elif cantidad%5 == 0:
    (billete) = cantidad/5
    print('te doy',billete, 'billetes de 5')
else:
    print('no puedo darte esta cantidad')

    
