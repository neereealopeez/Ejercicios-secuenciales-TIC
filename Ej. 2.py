#Segundo ejercicio: Calcular el perímetro y área de un rectángulo dada su base y su altura.
base=0
altura=0

base= (int)(input("¿Cuál es su base? "))
altura= (int)(input("¿Cuál es su altura? "))

print("El área es:" , base*altura)
print("El perímetro es:", (2*altura)+(2*base))