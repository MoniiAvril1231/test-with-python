import os
nom = ""
ulec = 0
nlec = 0
kwat = 0
otros = 0
total = 0
resp = ""
con = 0
nom = input("ingrese su nombre: ")
    ulec = int(input("ingrese su ultima lectura: "))
    nlec = int(input("ingrese su nueva lectura: "))
    kwat = float(input("ingrese precio de kwatt; "))
    otros = int(input("Ingrese montos extras: "))
    total = (((ulec - nlec)*kwat) + otros)
    print("La bonificacion de: " + nom +" es: "+ str(total))

    ''''
    if tser>=1 and tser<=3:
        bon = sue * 0.02
    elif tser>=4 and tser<=5:
        bon = sue * 0.03
    else:
        bon = sue * 0.04
    print("La bonificacion de: " + nom +" es: "+ str(bon))
    resp = input("Desea continuar:")
    os.system('cls')
print("la cantidad de trabajadores calculados:"+str(con)) ''