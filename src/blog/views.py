from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView,View,TemplateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Blog, Comment, Likes
from blog.forms import CommentForm

import uuid




class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'blog/my_blogs.html'





class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image', )

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ', '_') + '_' + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'blog/blog_list.html'

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    
    already_liked = Likes.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False  


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog:blog_detail', kwargs={'slug':slug}))

    return render(request, 'blog/blog_details.html', context={'blog':blog, 'comment_form':comment_form, 'liked':liked, } )    

@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user

    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        like_post = Likes(blog=blog, user=user)
        like_post.save()
    return HttpResponseRedirect(reverse('blog:blog_detail', kwargs={'slug':blog.slug}))   


@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog:blog_detail', kwargs={'slug':blog.slug}))   


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image', )
    template_name = 'blog/edit_blog.html'

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'slug':self.object.slug})





