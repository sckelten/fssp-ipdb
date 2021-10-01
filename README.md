# API БДИП ФССП России #

## Документация: ##
* [Регистрация пользователя API](https://api-ip.fssprus.ru/register)
* [Описание системы API](https://api-ip.fssprus.ru/about)
* [Справочник API](https://api-ip.fssprus.ru/swagger)

## Условия предоставления доступа к API ##
Выдержка из [описания системы API](https://api-ip.fssprus.ru/about).
<p>Максимальное число подзапросов в групповом запросе — 50 (если требуется отправить большее число, следует разбивать запрос на несколько)</p>
<p>Максимальное число одиночных запросов в час — 100. (Ограничение на одиночные запросы считается, как минус час от текущего времени)</p>
<p>Максимальное число одиночных запросов в сутки — 1000. (Ограничение на одиночные запросы считается, как минус сутки от текущего времени)</p>
<p>Максимальное число групповых запросов в сутки — 5000</p>

Срок хранения результатов запроса (промежуток между обращениями к методам /search/ и методу /result) — 24 часа.

## Назначение ##

Библиотека позводляет осуществлять групповой запрос к REST-API Банка данных исполнительных производств ФССП России.

Библиотека разработана с применением встроенного модуля urllib, без использования модуля Requests.

## Использование ##

1.  Пройти процесс регистрации и получить api-ключ.
2.  Сформировать csv-файл с данными для группового запроса по следующему шаблону:

| type* |      number*     | lastname* | firstname* | secondname |  birthdate  | region* |
|-------|------------------|-----------|------------|------------|-------------|---------|
|   1   |                  |  Иванов   |    Иван    |  Иванович  |  01.01.1990 |    43   |
|   3   | 123/21/43046-ИП  |           |            |            |             |         |

Поля, отмеченные "*" обязательны для заполнения.

Файл сохранить на жесткий диск. Для простоты можно поместить файл в директорию в библиотекой.

3. Запуск через терминал:

```
<work dir>\python main.py
```
```
Enter api key: [Ваш api-ключ]
```
```
Enter csv file name: [Путь к csv-файлу]
```
Результат выполнения запроса будет помещен в папку "out" (или в папку, указанную в файле settings.ini) в формате json.
