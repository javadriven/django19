from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.


def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request, id):
    # instance = Post.objects.get(id=10)
    instance = get_object_or_404(Post, id=id)

    context = {
        'title': 'Detail',
        'instance': instance
    }

    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()

    context = {
        'object_list': queryset,
        'title': 'List of Posts'
    }

    return render(request, "index.html", context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")