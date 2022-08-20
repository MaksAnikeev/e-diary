# Электронный дневник школы

Этот сайт - интерфейс для учеников школы. Здесь можно посмотреть оценки, расписание и прочую открытую информацию. Учителя заполняют базу данных через другой сайт. Ставят там оценки и т.д.

Данный проект позволяет изменять оценки в электронном дневнике, убирать "замечания" и добавлять "похвалу" выбранным ученикам.

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте БД командой `python3 manage.py migrate`
- Скопируйте в папку с файлом `manage.py` базу данных с оценками учеников `schoolbase.sqlite3`
- Запустите сервер командой `python3 manage.py runserver`
Вы увидите:
```py
System check identified no issues (0 silenced).
August 20, 2022 - 12:29:09
Django version 2.2.24, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Сайт будет доступен по адресу http://127.0.0.1:8000/
Чтобы остановить работу сервера нажмите `Crtrl C`

## Внесение изменений в дневник
Для внесения изменений необходимо запустить:
`python3 manage.py shell`
И последвательно запустить каждую строчку:
```py
import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation
from script import fix_marks, remove_chastisements, create_commendation
```
### Функции изменения данных
`fix_marks(name)` - функция меняет все 2 и 3 на 4 и 5, необходимо передать имя и фамилию ученика и запустить функцию `fix_marks(name='Фролов Иван')`

`remove_chastisements(name)` - функция удаляет все замечания учителей, необходимо передать имя и фамилию ученика и запустить функцию `remove_chastisements(name='Фролов Иван')`

`create_commendation(name, subject, lesson_date)` - функция добавляет похвалу на выбранный предмет и дату, 
необходимо передать имя и фамилию ученика, наименование предмета, дату и запустить функцию `create_commendation(name='Фролов Иван', subject='Музыка', lesson_date='2019-01-15')`

Если в школе несколько учеников с таким именем, то выскачит предупреждение об этом, тоже произойдет если в школе нет ученика с таким именем.

Для просмотра изменений выходим из shell командой `quit` и запускаем сервер командой `python3 manage.py runserver`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
