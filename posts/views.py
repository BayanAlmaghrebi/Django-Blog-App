from django.shortcuts import render
from .models import Post , Comment



def post_list(request): 
    data = Post.objects.all() # list
    return render(request,'all_post.html',{'posts':data})  # 3 (request, 'html', context{})




def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'post.html',{'post':data})