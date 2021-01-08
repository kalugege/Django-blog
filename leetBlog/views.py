from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comments
from django.urls import reverse_lazy
from .forms import Comment,PostForm
from django.contrib.messages.views import SuccessMessageMixin 



class Home(ListView):
    model = Post
    template_name = 'home.html'

class PostView(DetailView):
    model = Post
    template_name = 'postview.html'   

class AddPost(SuccessMessageMixin,CreateView):
    model = Post
    form_class = PostForm   
    template_name = 'addPost.html'
    success_message = 'post added!'
    # fields = '__all__'       

class UpdatePost(SuccessMessageMixin,UpdateView):
    model = Post
    template_name = 'update.html'
    success_message = 'updated!'
    fields = ['title','content']

class DeletePost(SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'delete.html'
    success_message = 'deleted'
    success_url = reverse_lazy('home')
         
class AddComment(CreateView):
    model = Comments
    form_class = Comment
    template_name = 'add-comment.html'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')
    