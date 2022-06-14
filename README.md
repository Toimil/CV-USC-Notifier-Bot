# CV-USC-Notifier-Bot

CV-USC-Notifier-Bot es un bot que muestra una notificación por pantalla cada vez que se realiza un cambio en el [Campus Virtual de la USC](cv.usc.es) en las asignaturas indicadas por el usuario.


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

    * Deberás indicar las URLs de las asignaturas de las cuales quieres ser notificado cuando se realice un cambio en estas, por ello, **modifica la lista *URLs***.
    * A su vez, debes **modificar la lista *subjectNames*** y poner el nombre de las asignaturas en el mismo orden en el que fueron introducidas las URLs.
    * Además, podrás modificar el icono con el que se ejecutará el bot e indicar la imagen que quieras.
    * Por último, **debes indicar tu correo electrónico y tu contraseña del campus virtual así como tu *execution***. Para obtener lo mencionado anteriormente, se ha facilitado un [*tutorial*](#tutorial-para-obtener-tu-execution).

4. Ejecuta el script mediante el comando **```python3 notificaciones_cv.py```**

5. Cuando desees finalizar la ejecución del bot tendrás que hacer ***click izquierdo*** en el icono y pulsar la opción ***Salir***.


## Tutorial para obtener tu *"execution"*

1. En primer lugar, accede a la web [cv.usc.es](https://login.usc.es/cas/login?service=https%3A%2F%2Fcv.usc.es%2Flogin%2Findex.php) y escribe tus credenciales como si estuvieras realizando un login normal.

2. Antes de pulsar *Identificarse* haz click derecho y selecciona ***Inspeccionar*** o si lo prefieres puedes hacer la combinacion de teclas ***```Ctrl + Shift + I```***.

3. Ahora la secuencia de pasos variará dependiendo del navegador que estés utilizando. A continuación, se muestra como se realizaría para Google Chrome y Mozilla Firefox.

   * Google Chrome:
      <p align="center">
        <img src="https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Explicaciones/explicacion_chrome.gif" alt="animated" />
      </p>
    * Mozilla Firefox:
      <p align="center">
        <img src="https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Explicaciones/explicacion_firefox.gif" alt="animated" />
      </p>


## Aviso

**Si el bot deja de funcionar o las notificaciones salen sin motivo alguno es porque es necesario volver a introducir otro nuevo valor para *execution* en el código, para ello volver a repetir el proceso descrito anteriormente**


## Hecho con

* [Python 3](https://www.python.org/)
* [Selenium Webdriver](https://www.selenium.dev/projects/)

## Autor

* **Óscar Toimil** - [Toimil](https://github.com/Toimil)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
