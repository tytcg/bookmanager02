from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo


def create_book(request):
    BookInfo.objects.create(name="十万个为什么", pub_date="2000-1-1",readcount=29)
    return HttpResponse("create")