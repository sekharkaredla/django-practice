
from django.shortcuts import render,redirect

from django.views import View

from .models import Post



from django.http import HttpResponse
# Create your views here.

class IndexPage(View):
    def get(self,request):
        all_posts = Post.objects.filter(private = False)
        return render(request,'feed.html',{'posts' : all_posts})

class AddLike(View):
    def post(self,request):
        output_dict = {}
        id_to_be_liked = request.POST.get('id')
        post_liked = Post.objects.get(id = id_to_be_liked)
        post_liked.likes += 1
        post_liked.save()
        return redirect('/insta')
