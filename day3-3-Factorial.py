"""
Escribe un programa que solicite al usuario un número entero no negativo 
y calcule su factorial. El factorial de un número entero positivo 'n' se define 
como el producto de todos los enteros desde 1 hasta 'n'. Utiliza un bucle para 
realizar el cálculo y muestra el resultado. Si el usuario ingresa un número negativo, 
muestra un mensaje de error y pide un número válido.
"""

numero=int(input("Ingresa un numero para saber su factorial: "))

#evaluamos el numero
if (numero>0):
    #definimos el decrementador
    bajo=numero-1
    actual=numero
    #Ciclo para que cuando sea 1 se ejecute y se salga
    while(bajo>=1):
        actual=(actual*bajo)
        bajo-=1
    
    print(f"El factorial de {numero} es = {actual}")    

else:
    print("\nEl numero que ingresaste no es positivo")
    print("Ya no quiero jugar contigo")