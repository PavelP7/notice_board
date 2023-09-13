<a name="readme-top"></a>
<h3 align="center">Доска объявлений </h3>

  <p align="center">
    Интернет-ресурс для фанатского сервера MMORPG.
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
## Содержание
1. [О проекте](#О-проекте)
   * [Стек](#Стек)
1. [Начало работы](#Начало-работы)
   * [Установка](#Установка)
1. [Как пользоваться](#Как-пользоваться)
   * [Регистрация](#Регистрация)
   * [Авторизация](#Авторизация)
   * [Объявления](#Объявления)
   * [Личный кабинет](#Личный-кабинет)
1. [Дополнительно](#Дополнительно)

<!-- ABOUT THE PROJECT -->
## О проекте

Проект представляет собой сервис по формированию объявлений зарегистрированными пользователями.

Проект предоставляет следующие возможности:
* Регистрацию по коду и паролю
* Авторизацию на сервере
* Создание объявлений
* Создание отклика на объявление
* Управление откликами в личном кабинете.

<p align="right">(<a href="#readme-top">наверх</a>)</p>



### Стек

* [![Python][Python.com]][Python-url]
* [![Django][Django.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![TyniMCE][TyniMCE.com]][TyniMCE-url]
* [![Apscheduler][Apscheduler.com]][Apscheduler-url]

<p align="right">(<a href="#readme-top">наверх</a>)</p>



<!-- GETTING STARTED -->
## Начало работы

Перед установкой и запуском проекта Вам необходимо установить **git**.

### Установка

Выполните следующие шаги для корректной установки проекта.
1. Клонируйте репозиторий
```sh
git clone https://github.com/PavelP7/notice_board.git
```
2. Установите требуемую версию **python** из файла *pythonversion.txt*
3. Перейдите в каталог *notice_board*, создайте и активируйте виртуальную среду
```sh
cd notice_board
python -m venv venv
venv\scripts\activate
```
4. Установите необходимые модули
```sh
pip install -r requirements.txt
cd NoticeBoard
```
5. Создайте файл *.env* с переменными среды из файла *.env.example* в этой же директории

<p align="right">(<a href="#readme-top">наверх</a>)</p>

<!-- USAGE EXAMPLES -->
## Как пользоваться
Запустите сервер при помощи команды ```python manage.py runserver```

### Регистрация
Регистрация пользователя доступна по адресу ```http://127.0.0.1:8000/sign/signup/```.  После ввода данных на указанный email будет отправлено письмо с четырехзначным кодом для подтверждения регистрации. Также будет автоматически предоставлена форма для подтверждения.

<p align="right">(<a href="#readme-top">наверх</a>)</p>

### Авторизация
Авторизация пользователя доступна по адресу ```http://127.0.0.1:8000/sign/login/```.  После успешной авторизации пользователю будет предоставлена возможность создания объявления, а также доступ в личный кабинет.

<p align="right">(<a href="#readme-top">наверх</a>)</p>

### Объявления
Работа с объявлениями доступна по адресу ```http://127.0.0.1:8000/board/```.  Для создания объявления авторизованному пользователю необходимо нажать ```Добавить объявление```. Для просмотра необходимо нажать на заголовок объявления, при этом будет осуществлен переход по адресу ```http://127.0.0.1:8000/board/<pk>/```, где ```<pk>``` - идентификатор объявления. 

На странице просмотра есть возможность оставить отклик на объявление. При создании отклика, на email автора объявления приходит уведомление.

<p align="right">(<a href="#readme-top">наверх</a>)</p>

### Личный кабинет
Переход в личный кабинет осуществляется по адресу ```http://127.0.0.1:8000/board/dashboard/```.  На данной странице пользователю предоставляется возможность управлять откликами на собственные объявления, а именно: 
+ сортировка по дате, пользователю и статусу
+ принятие отклика
+ удаление отклика.

В случае принятия на email автора отклика объявления приходит уведомление.


<p align="right">(<a href="#readme-top">наверх</a>)</p>

## Дополнительно
1. С целью выполнения периодических задач в проект добавлен планировщик *Apscheduler*. Для запуска необходимо выполнить
 ```sh
python manage.py runapscheduler.py
```
Планировщик выполняет следующие задачи:
+ рассылку каждый понедельник всем зарегистрированным пользователям списка новых объявлений за последнюю неделю
+ удаление каждую минуту информацию о незарегистрированных пользователях.
2. В проект также добавлен *WYSIWYG* редактор *TinyMCE*, для более удобного формирования объявлений.
<p align="right">(<a href="#readme-top">наверх</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Apscheduler.com]: https://img.shields.io/badge/apscheduler-white?style=for-the-badge&logo=apscheduler&logoColor=green
[Apscheduler-url]: https://apscheduler.readthedocs.io
[Django.com]: https://img.shields.io/badge/Django-white?style=for-the-badge&logo=django&logoColor=red
[Django-url]: https://github.com/django
[Python.com]: https://img.shields.io/badge/python-white?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://python.org 
[TyniMCE.com]: https://img.shields.io/badge/TinyMCE-white?style=for-the-badge&logo=tinymce&logoColor=blue
[TyniMCE-url]: https://www.tiny.cloud
[Bootstrap.com]: https://img.shields.io/badge/bootstrap-white?style=for-the-badge&logo=bootstrap&logoColor=violen
[Bootstrap-url]: https://bootstrap5.ru/
