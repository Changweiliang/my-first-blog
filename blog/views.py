from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse


def post_list(request):
    return render(request, 'blog/post_list.html', {})
