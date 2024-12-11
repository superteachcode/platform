# Superteach

Онлайн-платформа для репетиторов и учеников с конструктором заданий и системой оценок

## Как устроена

### Архитектура

- **Контейнеризация:** Docker

### Фронтенд

- **Языки:** HTML, CSS, JS, Typescript

- **Фреймворк:** Svelte 5 + Sveltekit

- **Тесты:** Vitest, Playwright

### Бэкенд

- **Язык:** Python 3.12.8

- **Фреймворк:** Django

- **Библиотеки:** Djangokit, Djapy, Pydantic

- **База данных:** PostgresSQL


## Как установить

Посмотреть текущую версию платформы можно после установки локальной версии.

Чтобы установить локальную версию:

1. Скачайте и установите [Python 3.12.8](https://www.python.org/downloads/release/python-3128/)

    > _Обратите внимание:_ на других версиях Python проект может не запуститься.

3. Клонируйте исходный код платформы командой:

    ```sh
    git clone git@github.com:superteachcode/platform.git
    ```

4. Запустите `configure.sh` для первичной конфигурации проекта

5. Откройте консоль в распакованной папке

6. В зависимости от вашей ОС, по очереди напишите в консоль следующие команды:

    ```sh
    pnpm setup:win
    ```

    Или по отдельности:

    **Бэкенд**
    ```sh
    pip install virtualenv
    ```

    ```sh
    pip install aiosmtpd
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

    **Фронтенд**
    ```sh
    cd frontend
    ```

    ```sh
    pnpm i
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

7. Готово! Можете переходить по адресу [127.0.0.1:8000](http://127.0.0.1:8000/) и работать с локальной версией проекта.

## Как запустить

Для запуска проекта нужно ввести в консоль команду:

```sh
pnpm dev
```

Или запускать сервера по отдельности:

**Бэкенд**

```sh
cd backend && .\venv\Scripts\activate && python manage.py runserver
```

**Фронтенд**

```sh
cd frontend && pnpm dev
```

## Как собрать

Для сборки проекта в продакшен нужно ввести в консоль команду:

```sh
pnpm build
```

## Как тестить

Для тестирования проекта после сборки нужно ввести в консоль команду:

```sh
pnpm preview
```

## Браузеры

На данный момент мы поддерживаем браузеры следующих версий:

- Safari >= 15.4
- Chrome & Edge >= 105
- Firefox >= 121
