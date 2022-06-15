#!/usr/bin/env python3

'''
Bot que muestra una notificación cada vez que se realiza un cambio en el campus virtual de la USC en las URLs indicadas por el usuario

Instrucciones para un correcto funcionamiento del bot en https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/README.md


© 2022 Toi1000, Santiago de Compostela, España © 
'''



# -----------------------------------------------------------------------------
# ------------------ MODIFICA ESTO CON TUS DATOS Y URLs -----------------------

URLs = ['https://cv.usc.es/course/view.php?id=27310',
        'https://cv.usc.es/course/view.php?id=27665',
        'https://cv.usc.es/course/view.php?id=27310',
        'https://cv.usc.es/course/view.php?id=27312',
        'https://cv.usc.es/course/view.php?id=27664',
        'https://cv.usc.es/course/view.php?id=28917']

# nombres de las asignaturas
subjectNames = ['COGA', 'ARQCOMP', 'BDII', 'DISEÑO', 'SOII', 'XEFE']

# imagen con el logotipo del icono
img = "logo.png"    

# completa con tu username, password y execution (disponible en github como obtener esta información)
payload = {
    'username': 'XXXXXXXXXX@rai.usc.es',
    'password': 'XXXXXXXXXX',
    'execution': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    '_eventId': 'submit',
    'geolocation': '', 
    'submit': 'Login3'
}
# -----------------------------------------------------------------------------





# realizamos los imports necesarios
import requests
import time
from win10toast import ToastNotifier
import pystray
import PIL.Image
import os
import ctypes


# comprobaciones
if (len(URLs) != len(subjectNames)):
    print("Error al introducir las URLs o los nombres de las asignaturas")
    print("Deben existir tantas URLs como nombres de asignaturas")
    os._exit(1)



def check_string(a):
    """Comprueba si existen las palabras 'Sen actividade recente' en el archivo pasado como parámetro
    return boolean true si esas palabras se encuentran en el archivo o false en caso contrario    
    """
    with open(a, encoding="utf-8") as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'Sen actividade recente' in line:
            return True
    return False


def on_clicked(icon, item):
    """Cuando se pulse en el item del icono se terminará el programa
    """
    icon.stop()
    os._exit(1)



toaster=ToastNotifier()   # notificacion
image=PIL.Image.open(img)  # abrimos la imagen
# creamos el icono con un item que será salir
icon = pystray.Icon("ToiBot", image, menu=pystray.Menu(
    pystray.MenuItem("Salir", on_clicked)
))
tam = len(URLs) # número de URLs



def cv(icon):
    """Realizamos el login en el campus virtual de la USC y comprobamos si se realizaron cambios en las URLs indicadas previamente
            en el caso de que se haya hecho un cambio, mostramos una notificación por pantalla
    """
    icon.visible = True
    with requests.Session() as s:
        while(1):

            p = s.post('https://login.usc.es/cas/login', data=payload) # logeamos en el campus virtual


            for i in range(tam):
                r = s.get(URLs[i])
                file = open(subjectNames[i] + ".txt", "w", encoding="utf-8")
                file.write(r.text) 
                if not check_string(subjectNames[i] + ".txt"):
                    toaster.show_toast("Campus Virtual", subjectNames[i], duration=30)
           
            time.sleep(60.0) # cada minuto comprobamos si se realizó algún cambio

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 ) # ocultamos la terminal para mejorar la experiencia del usuario

icon.run(cv)
