# CV-USC-Notifier-Bot

CV-USC-Notifier-Bot es un bot que muestra una notificación cada vez que se realiza un cambio en el [Campus Virtual de la USC](cv.usc.es) en las asignaturas de las cuales se indicó su URL.


## Por qué fue creado este bot?

Debido a que las notificaciones que llegan por correo avisando de cambios en el campus virtual (ya sean entregas, calificaciones o nuevas tareas) tardan a veces demasiado tiempo en ser recibidas, es de gran necesidad tener otra forma de enterarse de estos cambios de una manera mucho más inmediata.
Es por ello por lo que se decidió crear este bot.

## Compilación y ejecución

### Prerrequisitos

Necesitarás disponer de:

* Un espacio de trabajo con **Python**.

* Una versión de **Windows 10 o superior**.


### Ejecución del bot

1. Clona este repositorio en tu sistema mediante ```git clone https://github.com/Toimil/CV-USC-Notifier-Bot``` o descárgalo colocando todos los archivos en el mismo directorio.

2. Instala todas las librerias mencionadas en [requirements.txt](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/requirements.txt) y así asegurar un correcto funcionamiento del bot, para ello, ejecuta el siguiente comando ```pip install -r requirements.txt```

3. Modifica la primera parte del código [notificaciones_cv.py](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/notificaciones_cv.py) para adaptarlo a tus necesidades:

    * Deberás indicar las URLs de las asignaturas de las cuales quieres ser notificado cuando se realice un cambio en estas, para ello, modifica la lista *URLs*.
    * A su vez, debes modificar la lista *subjectNames* y poner el nombre de las asignaturas en el mismo orden en el que fueron introducidas las URLs.
    * Además, podrás modificar el icono con el que se ejecutará el bot e indicar la imagen que quieras.
    * Por último, debes indicar tu correo electrónico y tu contraseña del campus virtual así como tu *execution*. Para obtener lo mencionado anteriormente, podrás encontrar un tutorial a continuación.

4. Ejecuta el script mediante el comando **```python3 notificaciones_cv.py```**

5. Cuando desees finalizar la ejecución del bot tendrás que hacer *click izquierdo* en el icono y pulsar la opción *Salir*.

## Hecho con

* [Python 3](https://www.python.org/)
* [Selenium Webdriver](https://www.selenium.dev/projects/)

## Autores

* **Óscar Toimil** - [Toimil](https://github.com/Toimil)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
