#Programa para preguntar a un usuario su edad y si es mayor de 18 años mostrar un mensaje para dejarle pasar.
#Pregunto el nombre
nombre = input("Hola, ¿cómo te llamas?")
#Preguntamos su edad
edad = input(f"{nombre}, ¿cuántos años tienes?")
#Si su edad es 18 o más puede pasar y se mostrara en pantalla, si es menos no puede psar y se mostrara en pantalla.
if edad >= '18':
 print(f"{nombre}, you can come in.")
else:
 print(f"{nombre}, you can't come in.")