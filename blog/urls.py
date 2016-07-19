from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from blog.views import GreetingView, BlogView, AuthorDetailView, AuthorListView, AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    url(r'^$', GreetingView.as_view()),
    url(r'^baidu/$', RedirectView.as_view(pattern_name="google"), name='baidu'),
    url(r'^google/$', RedirectView.as_view(url="http://www.google.com.hk"), name='google'),
    url(r'^authors/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'author/add/$', AuthorCreate.as_view(), name='author-add'),
    url(r'author/(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author-update'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
    #url(r'^$', login_required(GreetingView.as_view())),

]
