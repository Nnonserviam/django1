from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'productos.html', { 'posts': posts })

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': post })

def product_list_view(request):
        posts = Post.objects.all()
        return render(request, 'home.html', {'products': posts})

def home(request):
    return render(request, 'home.html')

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-date']