#Datos de temperaturas por semanas
temperatures = [
    [22, 24, 19, 21, 25, 23, 20],  # Semana 1
    [20, 22, 21, 23, 24, 22, 21],  # Semana 2
    [23, 21, 20, 22, 24, 25, 23]   # Semana 3
]

#Funcion para calcular la media
def calcular_media(lista):   
    suma = sum(lista)
    media = suma / len(lista)
    return media

#Calculamos la media semanal con los datos
def calcular_media_semanal(datos):
    medias_semanales = []
    for semana in datos:
        media_semana = calcular_media(semana)
        medias_semanales.append(media_semana)
    return medias_semanales

#Calcular la temperatura media por semana y mostrar el resultado
medias_semanales = calcular_media_semanal(temperatures)

#La i es una variable que corresponde al numero de la semana.
for i, media in enumerate(medias_semanales, 1):
    print(f"Temperatura media de la Semana {i}: {media:.2f}°C")

#Función para calcular el día más caluros de cada semana.
def dia_mas_caluroso(semana):
    indice_dia_mas_caluroso = semana.index(max(semana)) + 1
    return indice_dia_mas_caluroso

#Encontrar el día más caluroso de cada semana y mostrar el resultado
for i, semana in enumerate(temperatures, 1):
    dia_caluroso = dia_mas_caluroso(semana)
    print(f"El día más caluroso de la Semana {i} es el día {dia_caluroso}.")

#Función para calcular las semanas con valores entre 20 y 25
def semanas_entre_20_y_25(temperaturas):
    semanas_20_25 = []

    for i, semana in enumerate(temperaturas, 1):
        if all(20 <= temp <= 25 for temp in semana):
            semanas_20_25.append(i)

    return semanas_20_25

# Encontrar las semanas con temperaturas entre 20 y 25 e imprimir el resultado
semanas_20_25 = semanas_entre_20_y_25(temperatures)

#Mostramos por pantalla las semanas con la temperatura contenida entre estos valores si las hubiera
if semanas_20_25:
    print("Las semanas con temperaturas entre 20 y 25 son las semanas:", semanas_20_25)
else:
    print("No hay semanas con temperaturas entre 20 y 25.")

#Función para calcular los cambios de temperatura con el dia anterior.
def cambios_temperatura(temperaturas):
    cambios_por_semana = []

    for semana in temperaturas:
        cambios_dia_anterior = [0]  #Con esto suponemos que el cambio para el primer día es 0
        for i in range(1, len(semana)):
            cambio = semana[i] - semana[i - 1]
            cambios_dia_anterior.append(cambio)
        cambios_por_semana.append(cambios_dia_anterior)

    return cambios_por_semana

#Calcular los cambios de temperatura y mostrar el resultado
cambios_por_semana = cambios_temperatura(temperatures)

#Mostramos estos cambios por pantalla en una lista.
for i, cambios in enumerate(cambios_por_semana, 1):
    print(f"Cambios de temperatura para la Semana {i}:", cambios)





