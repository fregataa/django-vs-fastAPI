# Django Async & ASGI Test

## How to run Django default server

```
python manage.py runserver 9009
```

## How to run Uvicorn

Go to testproject dir where asgi.py module exists
and run the command.

```
gunicorn testproject.asgi:application -k uvicorn.workers.UvicornWorker
```
