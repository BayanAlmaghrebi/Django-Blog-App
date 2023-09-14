from django.shortcuts import redirect, render
from .models import Post , Comment
from .forms import PostForm



def post_list(request): 
    data = Post.objects.all() # list  # 1 :query
    return render(request,'all_post.html',{'posts':data})  # 3 (request, 'html', context{})
                        # 2 : html page   3 : context



def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'post.html',{'post':data})



def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect ('/blog/')

    else:
        form = PostForm()
    return render(request, 'add_post.html',{'form':form})


def edit_post(request,post_id):
    data = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect ('/blog/')

    else:
        form = PostForm(instance=data)
    return render(request, 'edit_post.html',{'form':form})



def delete_post(request,post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect ('/blog/')