***Language:***
- [Español](./README.md)
- English

# CV-USC-Notifier-Bot

CV-USC-Notifier-Bot is a bot that displays a notification on the screen each time a change is made in the [USC Virtual Campus](https://login.usc.es/cas/login?service=https%3A%2F%2Fcv.usc.es%2Flogin%2Findex.php) in the subjects indicated by the user.


## Why was this bot created?

Due to the fact that the notifications that arrive by mail advising of changes in the virtual campus (whether they are deliveries, grades or new tasks) sometimes take too long to be received, it is of great need to have another way to find out about these changes in a much more immediate way.

That is why it was decided to create this bot.

## Compilation and execution

### Prerequisites

You will need to have:

* A workspace with **Python**.

* A version of **Windows 10 or higher**.


### Bot execution

1. Clone this repository to your system using ```git clone https://github.com/Toimil/CV-USC-Notifier-Bot``` or download it by putting all the files in the same directory.

2. Install all the libraries mentioned in [requirements.txt](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/requirements.txt) and thus ensure proper functioning of the bot, to do so, run the following command ```pip install -r requirements.txt```

3. Modify the first part of the [notificaciones_cv.py](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/notificaciones_cv.py) code to suit your needs:

    * You must indicate the URLs of the subjects of which you want to be notified when a change is made in them, therefore, **modify the *URLs* list**.
    * Also, you must **modify the *subjectNames* list** and put the names of the subjects in the same order in which the URLs were entered.
    * In addition, you can modify the icon with which the bot will be executed and indicate the image you want.
    * Finally, **you must indicate your e-mail and your virtual campus password as well as your *execution***. To get the above, a [*tutorial*](#tutorial-to-get-your-execution) has been provided.

4. Run the script using the command **```python3 notifications_cv.py```**.

5. When you want to end the execution of the bot you will have to ***right click*** on the icon and press the ***Salir*** option.


## Tutorial to get your *"execution"*

1. First, access the web [cv.usc.es](https://login.usc.es/cas/login?service=https%3A%2F%2Fcv.usc.es%2Flogin%2Findex.php) and type your credentials as if you were performing a normal login.

2. Before pressing *Identificarse*, right click and select ***Inspect*** or if you prefer you can do the key combination ***```Ctrl + Shift + I```***.

3. Now the sequence of steps will vary depending on the browser you are using. Below is how it would be done for Google Chrome and Mozilla Firefox.

   * Google Chrome:
      <p align="center">
        <img src="https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Explicaciones/explicacion_chrome.gif" alt="animated" />
      </p>
    * Mozilla Firefox:
      <p align="center">
        <img src="https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Explicaciones/explicacion_firefox.gif" alt="animated" />
      </p>

## Screenshots of the execution
   
![](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Screenshots/2817.jpg)        ![](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Screenshots/2818.jpg)

## Warning

**If the bot stops working or the notifications appear for no reason, it is because it is necessary to re-enter another new value for *execution* in the code, to do so repeat the process described above**.

## Possible improvements

In the future, it would be of great interest to modify the bot so that it is multiplatform, that is, that it can be used in addition to Windows on other systems such as various Linux distributions.

Also, another possible improvement to make is to host the bot on a server so that the computer does not have to be on all the time continuously executing the script.

## Made with

* [Python 3](https://www.python.org/)
* [Win10Toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
* [Pystray](https://github.com/moses-palmer/pystray)

## Author

* **Óscar Toimil** - [Toimil](https://github.com/Toimil)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
