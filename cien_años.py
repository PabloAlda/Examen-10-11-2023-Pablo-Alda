#Programa en el que preguntamos la edad al usuario y su nombre y le decimos el año en el que va a llegar a los 100.
#Pregunto el nombre
nombre = input("Hola, ¿cómo te llamas?")
#Preguntamos su edad
edad = float(input(f"{nombre}, ¿cuántos años tienes?"))
#Operación para calcular el año en el que llega a los 100
ano = 100 + 2023 - edad
#Mostramos ese año por pantalla
print(f"{nombre}, llegaras a los 100 años exacatamente el año:{ano}")