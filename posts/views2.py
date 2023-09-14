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