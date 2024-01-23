#Programa para convertir temperaturas
try:
    while(True):
        try:
            print("Vamos a convertir datos de temperatura")
            tipo = int(input("Cual es el tipo de dato que tienes? 1=Celcius . 2=Farenheit: "))
            temperatura = float(input("Cual es la temperatura que quieres convertir?: "))

            if (tipo == 1):
                resultado = ((temperatura*(9/5))+32)
                print(f"\nEl resultado de convertir {temperatura}°C es {resultado}°F\n")

            elif (tipo == 2):
                resultado = ((temperatura-32)*(5/9))
                print(f"\nEl resultado de convertir {temperatura}°F es {resultado}°C\n")
                
            else:
                print("\nNo ingresaste identificador de temperatura correcto\n")
            print("Calculo completado...\n\n")
        
        except(ValueError):
            print("\n=== Ingresaste un texto y yo necesito un numero ===\n")
except(KeyboardInterrupt):
    print("\n\n\t** Programa detenido por el usuario**\n")
    