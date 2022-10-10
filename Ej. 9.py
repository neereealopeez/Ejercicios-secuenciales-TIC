#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
total=0
descuento=0

total= (int)(input("¿Cuál es el total de la compra? "))
descuento= (total * 0.15)

print("Lo que el cliente deberá pagar es", (total-descuento))