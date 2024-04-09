import cv2
import face_recognition as fr 
import os
import numpy
from datetime import datetime

#crear base de datos

ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

#codificar imagenes
def codificar(imagenes):

    #crear una lista nueva
    lista_codificada = []

    #pasar todas las imagenes en RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        #codificacion
        codificado = fr.face_encodings(imagen)[0]

        #agregar a la lista
        lista_codificada.append(codificado)

    #devolver lista codificada
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)

#registrar ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_regitro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_regitro.append(ingreso[0])
    if persona not in nombres_regitro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H: %M: %S')
        f.writelines(f'\n{persona}, {string_ahora}')

#tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#leer la imagen capturada
exito, imagen = captura.read()

#LO HICE POR Q NO ME TOMA LA CAMARA :(
fotoFake = fr.load_image_file('Empleados\Ted Mosby.jpeg')
imagen = fotoFake


if not exito:
    print(f'No se ha podido tomar la captura correctamente')
else:
    #reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    #codificar la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    #buscar coincidencia con la base de caras

    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        
        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        #mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print ('No coincide con ninguno de nuestros empleados')
        else:
            
            #buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]
            print (f'Bienvenido/a al trabajo {nombre}')

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (255,0,0), 2)
            cv2.rectangle(imagen, (x1,y2 - 35), (x2, y2), (255,0,0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 +6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))

            #llamar la funcion para reg ingresos
            registrar_ingresos(nombre)
            #mostrar la imagen obtenida
            cv2.imshow('Imagen Web', imagen)
            #mantener ventana abierta
            cv2.waitKey(0)