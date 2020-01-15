import os
nom = ""
sue = 0
tser = 0
bon = 0
resp = ""
con = 0
while resp!="N":
    nom = input("ingrese su nombre: ")
    sue = int(input("ingrese su sueldo: "))
    tser = int(input("tiempo de servicio: "))
    con = con + 1
    if tser>=1 and tser<=3:
        bon = sue * 0.02
    elif tser>=4 and tser<=5:
        bon = sue * 0.03
    else:
        bon = sue * 0.04
    print("La bonificacion de: " + nom +" es: "+ str(bon))
    resp = input("Desea continuar:")
    os.system('cls')
print("la cantidad de trabajadores calculados:"+str(con))