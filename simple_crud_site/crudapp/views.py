from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from crudapp.models import Posts

def index(request):
    if request.method == "GET":
        datas = Posts.objects.order_by("-date")
        if len(datas) != 0:
            return render(request, "index.html", context={"posts":datas})
        else:
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
        return redirect('/')

def read(request):
    try:
        id = int(request.GET.get('id'))
        article = Posts.objects.filter(id=id)[0]
    except:
        return redirect('/')
    return render(request, "read.html", context={"article":article})
