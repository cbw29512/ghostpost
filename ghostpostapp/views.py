from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpostapp.models import PostItem
# Create your views here.


def index(request):
    data = PostItem.objects.all()
    return render(request, 'index.html', {'data':data})


def post_item(request):
    return render(request, 'index.html')


def like_view(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.likes += 1
    post.save


def post_details(request, id):
    html = 'index.html'
    post = PostItem.objects.get(id=id)
    return render(request, html, {'post': post})    
