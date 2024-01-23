#Programa para determinar si un numero es primo o no

print("\t\nBuen dia! Bienvenido a la calculadora de numeros primos!!\n") 

def numeroprimo(numero):
    contador=0
    if numero <=1:
        print("El numero NO puede ser menor que 2 o negativo! :/\n")    
    elif numero == 2:
        print("El numero 2 SI es primo\n")
    else:
        for divisor in range(2,int((numero/2)+1)):          #Esta division optimiza los recursos
            if(numero%divisor==0):
                contador+=1                                 #El contador nos ayuda a saber si ocurrio una division con % de 0
                
        if(contador>0):
            print(f"El numero {numero} NO es primo!!\n")
        else:
            print(f"El numero {numero} SI es primo\n")
try:
    while(True):
        try:            
            while(True):
                dato = int(input("Ingresa un numero para saber si es primo...: "))
                numeroprimo(dato)
        except(ValueError,NameError):
            print("Ingresaste un texto y yo necesito un numero para trabajar\n")
except(KeyboardInterrupt):
    print("\t ** Programa detenido por el usuario ** \n")