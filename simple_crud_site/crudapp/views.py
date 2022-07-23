from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from crudapp.models import Posts

def index(request):
    if request.method == "GET":
            return render(request, "index.html")

def create(request):
    if request.method == "GET":
        return render(request, "create.html")
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        content = request.POST.get("content")
        p = Posts(title=title, author=author, content=content, date=timezone.now())
        p.save()
        return HttpResponse("<h1>success</h1>")