#Tercer Ejercicio: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1=0

cateto2=0

import math

cateto1= (int)(input("¿Primer cateto? "))

cateto2= (int)(input("¿Segundo cateto? "))

print("La hipotenusa es", math.sqrt(((cateto1**2)+(cateto2**2))))