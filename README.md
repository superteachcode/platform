# Superteach

Онлайн-платформа для репетиторов и учеников с конструктором заданий и системой оценок
<!-- <p align="center">
<a href="https://sonniy.notion.site/72491004fa1044d8b0dccf9cdeb44053">Подробнее о проекте</a>⠀⠀
<a href="https://sonniy.notion.site/b24de6d1c4c54b448d795778ced458ad?v=5a6fda7d65df4894bb2a323eb854213b">Бэклог</a>
</p> -->

## Как устроена

### Архитектура

- **Контейнеризация:** Docker

### Фронтенд

- **Языки:** HTML, CSS, JS, Typescript

- **Фреймворк:** Svelte 5 + Sveltekit

### Бэкенд

- **Язык:** Python 3.12.8

- **Фреймворк:** Django

- **База данных:** PostgresSQL
...

## Как установить

Посмотреть текущую версию платформы можно после установки локальной версии.

Чтобы установить локальную версию:

1. Скачайте и установите [Python 3.12.8](https://www.python.org/downloads/release/python-3128/)
    > _Обратите внимание:_ на других версиях Python проект может не запуститься.

2. Клонируйте исходный код платформы
    ```sh
    git clone git@github.com:repetitkovo/platform.git
    ```

3. Запустите `configure.sh` для первичной конфигурации проекта

4. Откройте консоль в распакованной папке

5. В зависимости от вашей ОС, по очереди напишите в консоль следующие команды:

    **Windows**
    ```sh
    pip install virtualenv
    ```

    ```sh
    cd backend
    ```

    ```sh
    python -m venv venv
    ```

    ```sh
    .\venv\Scripts\activate
    ```

    ```sh
    pip install -r requirements.txt
    ```

    ```sh
    python manage.py migrate
    ```

    ```sh
    python manage.py runserver
    ```

    <!-- **Mac OS**
    ```sh
    sudo pip3 install virtualenv
    ```

    ```sh
    python3 -m venv venv
    ```

    ```sh
    source venv/bin/activate
    ```

    ```sh
    pip3 install -r requirements.txt
    ```

    ```sh
    cd mamayapovar
    ```

    ```sh
    python3 manage.py runserver
    ```

    **Linux**
    ```sh
    pip install virtualenv
    ```

    ```sh
    python3 -m venv venv
    ```

    ```sh
    source venv/bin/activate
    ```

    ```sh
    pip install -r requirements.txt
    ```

    ```sh
    cd mamayapovar
    ```

    ```sh
    python3 manage.py runserver
    ``` -->

6. Готово! Можете переходить по адресу [127.0.0.1:8000](http://127.0.0.1:8000/) и работать с локальной версией проекта.
    > Если вы запускаете локальную версию, то _уже загруженные изображения_ отображаться не будут, так как все пути в базе данных абсолютные, но если вы добавите свои рецепты, то все будет прекрасно работать!

## Как запустить

Для следующих запусков проекта нужно ввести в консоль команду:
<!--
**Windows**
```sh
npm run dev
```

**Mac OS**
```sh
source venv/bin/activate & cd mamayapovar & python3 manage.py runserver
```

**Linux**
```sh
source venv/bin/activate & cd mamayapovar & python3 manage.py runserver
``` -->

## Браузеры

На данный момент мы поддерживаем браузеры следующих версий:

- Safari >= 15.4
- Chrome & Edge >= 105
- Firefox >= 121
