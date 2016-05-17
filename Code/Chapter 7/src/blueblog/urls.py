from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from accounts.views import UserRegistrationView
from blog.views import NewBlogView
from blog.views import HomeView
from blog.views import UpdateBlogView
from blog.views import NewBlogPostView
from blog.views import UpdateBlogPostView
from blog.views import BlogPostDetailsView
from blog.views import SharePostWithBlog
from blog.views import StopSharingPostWithBlog
from blog.views import ShareBlogPostView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),

    url(r'^blog/new/$', NewBlogView.as_view(), name='new-blog'),
    url(r'^blog/(?P<pk>\d+)/update/$', UpdateBlogView.as_view(), name='update-blog'),
    url(r'blog/post/new/$', NewBlogPostView.as_view(), name='new-blog-post'),
    url(r'blog/post/(?P<pk>\d+)/update/$', UpdateBlogPostView.as_view(), name='update-blog-post'),
    url(r'blog/post/(?P<pk>\d+)/$', BlogPostDetailsView.as_view(), name='blog-post-details'),
    url(r'blog/post/(?P<pk>\d+)/share/$', ShareBlogPostView.as_view(), name='share-blog-post-with-blog'),
    url(r'blog/post/(?P<post_pk>\d+)/share/to/(?P<blog_pk>\d+)/$', SharePostWithBlog.as_view(), name='share-post-with-blog'),
    url(r'blog/post/(?P<post_pk>\d+)/stop/share/to/(?P<blog_pk>\d+)/$', StopSharingPostWithBlog.as_view(), name='stop-sharing-post-with-blog'),
]
