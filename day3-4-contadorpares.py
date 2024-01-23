"""
Escribe un programa que solicite al usuario un número entero positivo. 
Luego, utiliza un bucle para contar y mostrar la cantidad de números pares e impares 
en el rango desde 1 hasta el número ingresado por el usuario. Finalmente, muestra los resultados.
    Por ejemplo, si el usuario ingresa el número 10, el programa debe mostrar algo como:
    Números pares: 5
    Números impares: 5
"""
contadorpares=0
contadorimpares=0
numero = int(input("Ingresa un numero para contar numeros pares e impares desde ese al 1: "))

while (numero>=1):

    if ((numero)%2==0):
        contadorpares+=1
    elif (numero%2!=0):
        contadorimpares+=1
    numero-=1

print(f"Cantidad de numeros pares = {contadorpares}")
print(f"Cantidad de numeros impares = {contadorimpares}")