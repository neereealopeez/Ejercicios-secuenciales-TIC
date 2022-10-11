#Un alumno desea saber cual será su calificación final en la materia de  Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
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