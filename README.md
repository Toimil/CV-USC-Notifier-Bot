# CV-USC-Notifier-Bot

CV-USC-Notifier-Bot es un bot que muestra una notificación cada vez que se realiza un cambio en el [Campus Virtual de la USC](cv.usc.es) en las asignaturas de las cuales se indicó su URL.


## Por qué fue creado este bot?

Debido a que las notificaciones que llegan por correo de los cambios en el campus virtual ya sean entregas, notas o nuevas tareas tardan a veces demasiado tiempo es de necesidad tener otra manera de enterarse de estos cambios de una manera mucho más inmediata.

## Compilación y ejecución

### Prerrequisitos

Necesitarás disponer de:

* Un espacio de trabajo con **Python**.

* Una versión de **Windows 10 o superior**.


### Ejecución del bot

1. Clona este repositorio en tu sistema ```git clone https://github.com/Toimil/CV-USC-Notifier-Bot``` o descárgalo colocando todos los archivos en el mismo directorio

2. Instala todas las librerias mencionadas en requirements.txt para asegurar un correcto funcionamiento del bot ```pip install -r requirements.txt```

3. Modifica la primera parte del código [notificaciones_cv.py](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/notificaciones_cv.py) para adaptarlo a tus necesidades:

    * The default browser that it will try to use is Chromium. You can also tell it to open Firefox, via an argument: ```./backup.py -d firefox```
    * If you do not need the files from all grades, you can restrict the search so that just the files in a certain grade (4 in total) are downloaded, also via an argument; for instance, you can download files from the third grade using: ```./backup.py -g 3```

4. A window of the selected browser will automatically be opened. Do not close it, as the script requires it to explore the repository!

5. When the script has finished downloading the files, the browser will automatically be closed, therefore finishing the execution of the script.

## Built With

* [Python 3](https://www.python.org/)
* [Selenium Webdriver](https://www.selenium.dev/projects/)

## Authors

* **Álvaro Goldar Dieste** - [alvrogd](https://github.com/alvrogd)
* **D. Coladas** - [DColadas](https://github.com/DColadas)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
