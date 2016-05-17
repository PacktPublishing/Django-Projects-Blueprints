from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.text import slugify
from django.views.generic import CreateView
from django.http.response import HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import View

from blog.forms import BlogForm
from blog.forms import BlogPostForm
from blog.models import Blog
from blog.models import BlogPost


class NewBlogView(CreateView):
    form_class = BlogForm
    template_name = 'blog_settings.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if Blog.objects.filter(owner=user).exists():
            return HttpResponseForbidden ('You can not create more than one blogs per account')
        else:
            return super(NewBlogView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.owner = self.request.user
        blog_obj.slug = slugify(blog_obj.title)

        blog_obj.save()
        return HttpResponseRedirect(reverse('home'))


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            if Blog.objects.filter(owner=self.request.user).exists():
                ctx['has_blog'] = True
                blog = Blog.objects.get(owner=self.request.user)

                ctx['blog'] = blog
                ctx['blog_posts'] = BlogPost.objects.filter(blog=blog)
                ctx['shared_posts'] = blog.shared_posts.all()

        return ctx


class UpdateBlogView(UpdateView):
    form_class = BlogForm
    template_name = 'blog_settings.html'
    success_url = '/'
    model = Blog

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateBlogView, self).dispatch(request, *args, **kwargs)


class NewBlogPostView(CreateView):
    form_class = BlogPostForm
    template_name = 'blog_post.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NewBlogPostView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        blog_post_obj = form.save(commit=False)
        blog_post_obj.blog = Blog.objects.get(owner=self.request.user)
        blog_post_obj.slug = slugify(blog_post_obj.title)
        blog_post_obj.is_published = True

        blog_post_obj.save()

        return HttpResponseRedirect(reverse('home'))


class UpdateBlogPostView(UpdateView):
    form_class = BlogPostForm
    template_name = 'blog_post.html'
    success_url = '/'
    model = BlogPost

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateBlogPostView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(UpdateBlogPostView, self).get_queryset()
        return queryset.filter(blog__owner=self.request.user)


class BlogPostDetailsView(DetailView):
    model = BlogPost
    template_name = 'blog_post_details.html'


class ShareBlogPostView(TemplateView):
    template_name = 'share_blog_post.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ShareBlogPostView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, pk, **kwargs):
        blog_post = BlogPost.objects.get(pk=pk)
        currently_shared_with = blog_post.shared_to.all()
        currently_shared_with_ids = map(lambda x: x.pk, currently_shared_with)
        exclude_from_can_share_list = [blog_post.blog.pk] + list(currently_shared_with_ids)

        can_be_shared_with = Blog.objects.exclude(pk__in=exclude_from_can_share_list)

        return {
            'post': blog_post,
            'is_shared_with': currently_shared_with,
            'can_be_shared_with': can_be_shared_with
        }


class SharePostWithBlog(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SharePostWithBlog, self).dispatch(request, *args, **kwargs)

    def get(self, request, post_pk, blog_pk):
        blog_post = BlogPost.objects.get(pk=post_pk)
        if blog_post.blog.owner != request.user:
            return HttpResponseForbidden('You can only share posts that you created')

        blog = Blog.objects.get(pk=blog_pk)
        blog_post.shared_to.add(blog)

        return HttpResponseRedirect(reverse('home'))


class StopSharingPostWithBlog(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StopSharingPostWithBlog, self).dispatch(request, *args, **kwargs)

    def get(self, request, post_pk, blog_pk):
        blog_post = BlogPost.objects.get(pk=post_pk)
        if blog_post.blog.owner != request.user:
            return HttpResponseForbidden('You can only stop sharing posts that you created')

        blog = Blog.objects.get(pk=blog_pk)
        blog_post.shared_to.remove(blog)

        return HttpResponseRedirect(reverse('home'))