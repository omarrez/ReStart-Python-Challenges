"""
Mostrar todos los numeros primos entre 1 y 250.
Almacenar los numeros en un archivo results.txt
"""
print("\nEste programa va a mostrarte todos los numeros primos del 1 al 250")
print("Recordar que para que sea numero primo debe de ser positivo y de 2 en adelante...\n")

nameFile="results.txt"
doc = open(nameFile,"w")

for actual in range(2,151):
    EsPrimo = True
    for divisor in range(2,(int((actual/2)+1))):
        if (actual%divisor==0):
            EsPrimo=False
            
    if (EsPrimo == True):
        doc.write(f"{actual} es primo\n")

doc.close()