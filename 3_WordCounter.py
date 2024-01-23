#Programa para contar palabras

texto = input("Ingresa un texto para contar sus palabras: ")
contador=0
divido = texto.split(" ")
#print(divido)

for n in divido:
    contador+=1

print(f"El total de las palabras es: {contador}")