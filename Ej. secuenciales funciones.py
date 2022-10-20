print("Primer Ejercicio: Escribir un programa que pregunte al usuario su nombre, y luego lo salude.")
def ejer1():
    nombre="" 
    nombre=input("Dime tu nombre \n") 
    print("Tu nombre es", nombre,)
ejer1()

print("Segundo ejercicio: Calcular el perímetro y área de un rectángulo dada su base y su altura.")
def ejer2():
    base=0
    altura=0
    base= (int)(input("¿Cuál es su base? "))
    altura= (int)(input("¿Cuál es su altura? "))
    print("El área es:" , base*altura)
    print("El perímetro es:", (2*altura)+(2*base))
ejer2()

print("Tercer Ejercicio: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.")
def ejer3():
    cateto1=0
    cateto2=0
    import math
    cateto1= (int)(input("¿Primer cateto? "))
    cateto2= (int)(input("¿Segundo cateto? "))
    print("La hipotenusa es", math.sqrt(((cateto1**2)+(cateto2**2))))
ejer3()

print("Cuarto Ejercicio: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.")
def ejer4():
    num1=0
    num2=0
    num1= (int)(input("¿Cuál es el primer número? "))
    num2= (int)(input("¿Cuál es el segundo número? "))
    print("Su suma es", num1+num2)
    print("Su recta es", num1-num2, "o también", num2-num1)
    print("Su división es", num1/num2, "o también", num2/num1)
    print("Su multiplicación es", num1*num2)
ejer4()

print("Quinto Ejercicio: Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. ")
def ejer5():
    gradof=0
    gradoc=0
    gradof= (int)(input("¿Grados Fahrenheit? "))
    gradoc=(gradof-32)*5/9
    print("Son", gradoc, "ºC")
ejer5()

print("Sexto Ejercicio: Calcular la media de tres números pedidos por teclado.")
def ejer6():
    num1=0
    num2=0
    num3=0
    num1=(int)(input("¿Primer número? "))
    num2=(int)(input("¿Segundo número? "))
    num3=(int)(input("¿Tercer número? "))
    print("Su media es", (num1+num2+num3)/3)
ejer6()

print("Séptimo Ejercicio: Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.Por ejemplo: 1000 minutos son 16 horas y 40 minutos.")
def ejer7():
    def truncate(horas, decimals = 0): 
        multiplier = 10 ** decimals 
        return int(horas * multiplier) / multiplier 
    minutos=0
    horas=0
    minutos=(int)(input("¿Cuántos minutos quieres ingresar? \n"))
    horas=minutos/60
    print("Has ingresado", minutos , "minutos son" , (truncate(horas)), "horas y", ((10/horas)*60), "minutos")
ejer7()

print("Octavo Ejercicio:_Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto decomisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.")
