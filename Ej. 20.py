#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) 
# después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
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