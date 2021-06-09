import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

from asgiref.sync import sync_to_async

# from django.views import View

# from django.views.decorators.csrf import csrf_exempt

from testapp.models import Book, AsyncBook

# class BookView(View):

#     def get(self, request, *args, **kwargs):
#         print(request.GET)
#         print(args)
#         print(kwargs)
#         return HttpResponse("Get!")

# class BookListCreateView(View):

#     def get(self, request, *args, **kwargs):
#         print(request.GET)
#         print(args)
#         print(kwargs)
#         return HttpResponse("List!")

#     def post(self, request, *args, **kwargs):
#         print(request.POST)
#         print(json.loads(request.body))
#         print(args)
#         print(kwargs)
#         return HttpResponse("Book!")

# class AsyncBookView(View):

#     async def get(self, request, *args, **kwargs):
#         print(request.GET)
#         print(args)
#         print(kwargs)
#         return await HttpResponse("Get!")

# class AsyncBookListCreateView(View):


#     async def get(self, request, *args, **kwargs):
#         print(request.GET)
#         print(args)
#         print(kwargs)
#         return await HttpResponse("List!")

#     async def post(self, request, *args, **kwargs):
#         print(request.POST)
#         print(json.loads(request.body))
#         print(args)
#         print(kwargs)
#         return await HttpResponse("Book!")


def index(request):
    print(request.GET)
    return HttpResponse("Hello, world. You're at the polls index.")


def list_or_create_book(request, *args, **kwargs):
    if request.method == "GET":
        result = Book.objects.all()
        return HttpResponse(result)
    elif request.method == "POST":
        data = json.loads(request.body)
        print(data)
        result, _ = Book.objects.get_or_create(
            title=data["title"], author=data["author"], volume=data["volume"]
        )
        return HttpResponse(result)
    elif request.method == "DELETE":
        Book.objects.all().delete()
        return HttpResponse("Deleted")
    return HttpResponse("Wrong method")


def get_book(request, *args, **kwargs):
    result = Book.objects.get(id=kwargs["pk"])
    return HttpResponse(result)


# def _get_blog(pk):
#     return Blog.objects.select_related('author').get(pk=pk)

# get_blog = sync_to_async(_get_blog, thread_sensitive=True)

# def get_httpres(payload):
#     return HttpResponse(payload)


async def async_list_or_create_book(request, *args, **kwargs):
    if request.method == "GET":
        # return await sync_to_async(list_or_create_book, thread_sensitive=True)(request, *args, **kwargs)
        result = await sync_to_async(AsyncBook.objects.all, thread_sensitive=True)()
        return await sync_to_async(HttpResponse)(result)
        # return await HttpResponse(result)
    elif request.method == "POST":
        data = json.loads(request.body)
        result, _ = await sync_to_async(
            AsyncBook.objects.get_or_create, thread_sensitive=True
        )(title=data["title"], author=data["author"], volume=data["volume"])
        # return await sync_to_async(HttpResponse)(result)
        return HttpResponse(result)
    elif request.method == "DELETE":
        await sync_to_async(Book.objects.all().delete)()
        # return await sync_to_async(HttpResponse)("Deleted")
    return await sync_to_async(HttpResponse)("Wrong method")


async def async_get_book(request, *args, **kwargs):
    # print(request.GET)
    # print(args)
    # print(kwargs)
    result = await sync_to_async(AsyncBook.objects.get, thread_sensitive=True)(
        id=kwargs["pk"]
    )
    # await sync_to_async(print)(type(result.__dict__))
    return await sync_to_async(HttpResponse)(result)
