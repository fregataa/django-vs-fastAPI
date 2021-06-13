# Django Async & ASGI Test

## How to run Django default server with WSGI Gunicorn

```
python manage.py runserver
```

## How to run with Uvicorn

Go to testproject dir where asgi.py module exists
and run the command.

```
gunicorn testproject.asgi:application -k uvicorn.workers.UvicornWorker
```
