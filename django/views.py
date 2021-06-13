import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from asgiref.sync import sync_to_async

from django_app.models import Book, AsyncBook


def index(request):
    print(request.GET)
    return HttpResponse("Hello, world. You're at the polls index.")


def list_or_create_book(request, *args, **kwargs):
    _ = args
    _ = kwargs
    if request.method == "GET":
        result = Book.objects.all()
        return HttpResponse(result)
    elif request.method == "POST":
        data = json.loads(request.body)
        result, _ = Book.objects.get_or_create(
            title=data["title"], author=data["author"], volume=data["volume"]
        )
        return HttpResponse(result)
    elif request.method == "DELETE":
        Book.objects.all().delete()
        return HttpResponse("Deleted")
    return HttpResponse("Wrong method")


def get_book(request, *args, **kwargs):
    _ = args
    _ = kwargs
    result = Book.objects.get(id=kwargs["pk"])
    return HttpResponse(result)


async def async_list_or_create_book(request, *args, **kwargs):
    _ = args
    _ = kwargs
    if request.method == "GET":
        result = await sync_to_async(AsyncBook.objects.all, thread_sensitive=True)()
        return await sync_to_async(HttpResponse)(result)
    elif request.method == "POST":
        data = json.loads(request.body)
        result, _ = await sync_to_async(
            AsyncBook.objects.get_or_create, thread_sensitive=True
        )(title=data["title"], author=data["author"], volume=data["volume"])
        return HttpResponse(result)
    elif request.method == "DELETE":
        await sync_to_async(Book.objects.all().delete)()
    return await sync_to_async(HttpResponse)("Wrong method")


async def async_get_book(request, *args, **kwargs):
    result = await sync_to_async(AsyncBook.objects.get, thread_sensitive=True)(
        id=kwargs["pk"]
    )
    return await sync_to_async(HttpResponse)(result)
