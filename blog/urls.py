from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from blog.views import GreetingView, BlogView

urlpatterns = [
    url(r'^$', GreetingView.as_view()),
    url(r'^baidu/$', RedirectView.as_view(pattern_name="google"), name='baidu'),
    url(r'^google/$', RedirectView.as_view(url="http://www.google.com.hk"), name='google'),
    #url(r'^$', login_required(GreetingView.as_view())),

]
