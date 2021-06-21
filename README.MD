# Django Async & ASGI Test

## How to run Django

### With default WSGI

```
python manage.py runserver
```

### With Uvnicorn ASGI

Check [Django Official doc for Using Uvicorn](https://docs.djangoproject.com/ko/3.2/howto/deployment/asgi/uvicorn/) for more information.

```
gunicorn testproject.asgi:application -k uvicorn.workers.UvicornWorker
```

## How to run FastAPI

Change your directory to `/fastAPI`

```
python3 main.py
```
