Сервис читает параметры из таблицы `queue_requests`, отправляет запросы и записывает ответы в таблицу `queue_responses`.

Стек:
- asyncio
- requests
- threads
- sqlalchemy
- postgres
- docker

По заданию нужно использовать потоки, поэтому запросы отправляю не через `aiohttp`, а через `requests` в потоке.

```bash
git clone https://github.com/ipodprugin/send-requests-service.git && cd send-requests-service
cp example.env .env
```

Тестовые данные для таблицы `queue_requests` можно положить в `db/dbdata.sql`

## Запуск:

```bash
docker compose up
```
