from django.views import generic
from .models import Post


"""
    model_operation: means:
    template_name: post_list.html
    context_name: post_list or object_list
"""
class PostList(generic.ListView):
    model = Post



"""
    template_name: post_detail.html
    context : post , object
"""
class PostDetail(generic.DetailView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = '__all__'      # form
    success_url = '/blog/'


class PostEdit(generic.UpdateView):
    model = Post
    fields = '__all__'      # form
    success_url = '/blog/'
    template_name = 'posts/edit_post.html'


class PostDelete(generic.DeleteView):
    model = Post
    success_url = '/blog/'