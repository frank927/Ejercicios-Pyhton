# 1 Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def maximo(n1, n2):
    if(n1>n2):
        return n1
    elif(n2>n1):
        return n2
    else:
        raise Exception("Los valores son iguales")
#print(maximo(3,6))

# 2 Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(n1 , n2, n3):
    maximo=0
    lista=[n1, n2, n3]
    for l in lista:
        if(l>maximo):
            maximo=l
    print(maximo)
#max_de_tres(9,3,14)

# 3 Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def EsVocal():
      letra= input("Escriba solo un caracter: ")
      if(letra=="a"or letra=="e" or letra=="i"or letra=="o" or letra=="u" or letra=="A"or letra=="E" or letra=="I"or letra=="O" or letra=="U"):
          return True
      else:
          if(len(letra)>=2):
             raise Exception("Ingrese solo un caracter")
          else:
             return False
#print(EsVocal())

# 4 Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

lista=[1,2,3,4]
def suma():
    s=0
    for i in lista:
        s+=i
    return s

def multi():
    m=1
    for i in lista:
        m*=i
    return m

#print(suma())
#print(multi())

# 5 Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa():
    cadena=input("escriba algo: ")
    cadenaInvertida = cadena [:: - 1 ]
    print( cadenaInvertida )

#inversa()
    
# 6 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo():
    cadena="franknarf"
    mitad=len(cadena)/2
    if(len(cadena)%2!=0):
        medio=int(mitad)
        final=cadena[medio: ]
        finalInverso=final[:: -1]
        principio=cadena[ :medio+1]
        if(principio==finalInverso):
            print("Es Palindromo!!!")
        else:
            print("No es palindromo")
    else:
        medio=int(mitad)
        final=cadena[medio: ]
        finalInverso=final[:: -1]
        principio=cadena[ :medio]
        if(principio==finalInverso):
            print("Es Palindromo!!!")
        else:
            print("No es palindromo")
  
#es_palindromo()

# 7 Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

lista1=[1,21,34,47]
lista2=[5,6,7,8,9,34,54,12]
def superposicion():
    for i in lista1:
        for y in lista2:
            if(i==y):
                return True
    return False        
            
#print(superposicion())      

# 8 Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres():
    caracter= input("Ingrese un solo caracter: ")
    cantidad= int(input("Ingrese un multiplicador entero: "))
    if(len(caracter)>1):
        raise Exception("Solo se admite un caracter")
    elif(cantidad%2!=0 or cantidad<0):
        raise Exception("Solo se admiten numeros enteros positivos")
    else:
        return print(caracter*cantidad)

#generar_n_caracteres()
    
# 9 Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.

import matplotlib.pyplot as plot

def procedimiento():
    salarios = [1250, 1540, 1310, 1265, 1880, 2040, 1920, 2015, 1340]

    intervalos = [1000, 1500, 2000, 2500]

    plot.hist(x=salarios, bins=intervalos, color='#F2AB6D', rwidth=0.65,)
    plot.title('Histograma de salarios')
    plot.xlabel('Salarios')
    plot.ylabel('Frecuencia')
    plot.xticks(intervalos)

    plot.show()
    
#procedimiento()
    

    