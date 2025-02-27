# Пульт охраны банка

Учебный проект, задачами которого является:
+ подключение к базе данных охраны банка,
+ поиск подозрительных лиц, находящихся в хранилище длительное время,
+ вывод на сайт времени нахождения сотрудников в хранилище

### Как установить
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Дополнительно в каталоге с файлом `manage.py` следует создать файл `.env`, в который необходимо прописать:

```
ENGINE = название файла с базой данных django
HOST = адрес хоста подключения к базе данных
PORT = номер подключаемого порта
NAME = имя базы
USER = логин пользователя
PASSWORD = пароль
SECRET_KEY = пароль к Djungo
DEBUG = True или False, в зависимости от необходимости вывода ошибок на экран
```

### Как запустить

Программа запускается с командной строки:
```
python manage.py runserver
```
Результат программы можно увидеть в браузере, перейдя по адресу `127.0.0.1:8000`

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
