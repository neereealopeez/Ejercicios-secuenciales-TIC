#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de
# comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
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