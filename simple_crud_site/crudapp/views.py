import hashlib
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from crudapp.models import Posts, Comments

def index(request):
    if request.method == 'GET':
        datas = Posts.objects.order_by('-date')
        if len(datas) != 0:
            return render(request, 'index.html', context={'posts':datas})
        else:
            return render(request, 'index.html')

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        author_password = request.POST.get('author_password')
        content = request.POST.get('content')
        author_password = hashlib.sha256(author_password.encode()).hexdigest()
        p = Posts(title=title, content=content, date=timezone.now(), author=author, author_password=author_password)
        p.save()
        messages.success(request, 'post was uploaded')
        return redirect('/')

def read(request,id):
    article = get_object_or_404(Posts, pk=id)
    comments = article.comments_set.all()

    return render(request, 'read.html', context={'article':article, 'comments':comments})

def delete(request):
    if request.method != 'POST':
        return redirect('/')
    author = request.POST.get('author')
    author_password = hashlib.sha256(request.POST.get('author_password').encode()).hexdigest()
    id = int(request.POST.get('id'))
    article = Posts.objects.get(id=id)
    if author_password == article.author_password and author == article.author:
        article.delete()
        article.save()
    else:
        messages.error(request, 'Incorrect author information')
        return redirect('/')

def update(request,id):
    if request.method == 'GET':
        article = get_object_or_404(Posts, pk=id)
        return render(request, 'update.html', context={'article':article})

    if request.method == 'POST':
        author = request.POST.get('author')
        author_password = hashlib.sha256(request.POST.get('author_password').encode()).hexdigest()
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = get_object_or_404(Posts, pk=id)
        if author == article.author and author_password == article.author_password:
            article.title = title
            article.content = content
            article.save()
        else:
            messages.error(request, 'Incorrect author information')
        return redirect('/read/'+str(id))


def create_comment(request):
    author = request.POST.get("author")
    author_password = hashlib.sha256(request.POST.get("author_password").encode()).hexdigest()
    comment_content = request.POST.get("comment_content")
    id = int(request.POST.get("id"))
    p = get_object_or_404(Posts, pk=id)
    comment = Comments(post=p, comment_date=timezone.now(), author=author, author_password=author_password, comment_content=comment_content)
    comment.save()
    return redirect('/read/'+str(id))