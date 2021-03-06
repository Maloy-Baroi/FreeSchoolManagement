from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Blog.models import Blog, Comment, Likes
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from App_Blog.forms import CommentForm


# Create your views here.
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)
    queryset = Blog.objects.order_by('publish_date')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:my_blog'))


class BlogList(LoginRequiredMixin, ListView):
    context_object_name = 'Blog'
    model = Blog
    template_name = 'App_Blog/blog_list.html'


@login_required
def blog_details(request, slug):
    blog_slug = Blog.objects.get(slug=slug)
    print(blog_slug)
    commentform = CommentForm()
    already_liked = Likes.objects.filter(blog=blog_slug, user=request.user)
    if already_liked:
        like = True
    else:
        like = False
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.user = request.user
            comment.blog = blog_slug
            comment.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': slug}))
    return render(request, 'App_Blog/blog_details.html',
                  context={'blog': blog_slug, 'commentform': commentform, 'liked': like})


@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        like_post = Likes(blog=blog, user=user)
        like_post.save()
        return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': blog.slug}))


@login_required
def disliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug': blog.slug}))


class MyBlog(LoginRequiredMixin, TemplateView):
    template_name = 'App_Blog/my_blog.html'


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['blog_title', 'blog_content', 'blog_image', ]
    template_name = 'App_Blog/Edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug': self.object.slug})
