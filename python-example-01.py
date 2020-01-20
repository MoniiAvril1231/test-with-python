import os
nom = ""
total = 0
bon = 0
resp = ""
saldo = 15
con = 0
kwat = 0
while resp!="N":
    nom = input("ingrese su nombre: ")
    kwat = int(input("numero de kilowats consumidos: "))
    con = con + 1
    total = kwat*0.45 + saldo
    print("El monto a pagar de este mes de " + nom +" es: "+ str(float(total)))
    resp = input("Desea continuar:")
    os.system('cls')
print("la cantidad de trabajadores calculados:"+str(con))