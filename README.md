# CV-USC-Notifier-Bot

CV-USC-Notifier-Bot es un bot que muestra una notificación cada vez que se realiza un cambio en el [Campus Virtual de la USC](cv.usc.es) en las asignaturas de las cuales se indicó su URL.


## Por qué fue creado este bot?

Debido a que las notificaciones que llegan por correo de los cambios en el campus virtual ya sean entregas, notas o nuevas tareas tardan a veces demasiado tiempo es de necesidad tener otra manera de enterarse de estos cambios de una manera mucho más inmediata.

## Getting started

### Prerequisites

You will need:

* Any of the following **browsers**: Firefox, Chromium.

* A working installation of **Python 3**.

* The **```selenium``` module**, which is needed to control the browser, and which is not included by default in Python 3.
    * You can add it to your Python installation using: ```pip3 install selenium```.

### Running the script

1. Download the file ```backup.py```

2. Grant it execution permissions; one way would be running: ```chmod u+x ./backup.py```

3. Execute the script: ```./backup.py```

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
