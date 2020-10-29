from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Movie
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

def home(request):

    context =  {
         'posts': Post.objects.all()
    }

    # return HttpResponse('<h1>Blog Home</h1>')
    # Use a template instead of above!
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # ordering =  ['date_posted']
    # - sign reverse sort order! newest to oldest
    ordering =  ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

    def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
        return True
      return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
        return True
      return False

    

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request,'blog/about.html')


def movie(request):

    context =  {
         'movies': Movie.objects.all()
    }

    return render(request,'blog/movies.html', context)


