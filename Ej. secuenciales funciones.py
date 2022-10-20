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

print("Octavo Ejercicio: Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto decomisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.")
def ejer8():
    venta1=0
    venta2=0
    venta3=0
    sueldo=0
    totalv=0
    comisiones=0
    dinero=0
    venta1= (int)(input("¿Dinero ganado en la primera venta? "))
    venta2= (int)(input("¿Dinero ganado en la segunda venta? "))
    venta3= (int)(input("¿Dinero ganado en la tercera venta? "))
    sueldo= (int)(input("¿Sueldo recibido? "))
    totalv= (venta1 + venta2 + venta3)
    comisiones= (totalv * 0.1)
    dinero= (sueldo + comisiones)
    print("El total de las tres ventas es", totalv, ", las comisiones son", comisiones, "y el dinero total ganado es", dinero)
ejer8()

print("Noveno Ejercicio: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.")
def ejer9():
    total=0
    descuento=0
    total= (int)(input("¿Cuál es el total de la compra? "))
    descuento= (total * 0.15)
    print("Lo que el cliente deberá pagar es", (total-descuento))
ejer9()

print("Décimo Ejercicio: Un alumno desea saber cual será su calificación final en la materia de  Algoritmos. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales. 30% de la calificación del examen final. 15% de la calificación de un trabajo final.")
def ejer10():
    nota1=0
    nota2=0
    nota3=0
    examen=0
    trabajo=0
    promedio=0
    promediofinal=0
    nota1= (int)(input("¿Cuál es la primera nota? "))
    nota2= (int)(input("¿Cuál es la segunda nota? "))
    nota3= (int)(input("¿Cuál es la tercera nota? "))
    examen= (int)(input("¿Cuál es la calificación en el examen final? "))
    trabajo= (int)(input("¿Cuál es la nota  del trabajo? "))
    promedio= ((nota1+nota2+nota3)/3)
    promediofinal = (promedio * .55)+(examen * .30)+(trabajo * .15)
    print("El promedio final de la materia de algoritmos es:",round(promediofinal,1))
ejer10()

print("Vigésimo Ejercicio: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)  después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).")
def ejer20():
    euro2=0
    euro1=0
    cent50=0
    cent20=0
    cent10=0
    total_euros=0
    total_centimos=0
    euro2= (int)(input("¿Monedas de 2 euros? "))
    euro1= (int)(input("¿Monedas de 1 euro? "))
    cent50= (int)(input("¿Monedas de 50 céntimos? "))
    cent20= (int)(input("¿Monedas de 20 céntimos? "))
    cent10= (int)(input("¿Monedas de 10 céntimos? "))
    total_euros= ((euro2 * 2) + (euro1))
    total_centimos= ((cent50 * 0.50) + (cent20 * 0.20) + (cent10 * 0.10))
    print("El total de euros es", total_euros, "y de céntimos es", total_centimos)