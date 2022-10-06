#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

def truncate(horas, decimals = 0): 
    multiplier = 10 ** decimals 
    return int(horas * multiplier) / multiplier 
  
minutos=0
horas=0

minutos=(int)(input("¿Cuántos minutos quieres ingresar? \n"))

horas=minutos/60

print("Has ingresado", minutos , "minutos son" , (truncate(horas)), "horas y", ((10/horas)*60), "minutos")
