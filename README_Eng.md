# Bank security console

Educational project, the tasks of which are:
+ connection to the bank's security database,
+ search for suspicious persons who have been in storage for a long time,
+ output to the site of the time spent by employees in the warehouse

### How to install
Python3 should already be installed.
Then use `pip` (or `pip3`, there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```
Additionally, in the directory with the `manage.py` file, create a `.env` file, in which you need to write:

```
ENGINE = django database filename
HOST = database connection host address
PORT = number of connected port
NAME = database name
USER = username
PASSWORD = password
SECRET_KEY = Djungo password
DEBUG = True or False, depending on the need to display errors on the screen
```

### How to start

The program is launched from the command line:
```
python manage.py runserver
```
The result of the program can be seen in the browser by going to `127.0.0.1:8000`

### Objective of the project

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).