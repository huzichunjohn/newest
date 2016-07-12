from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from blog.views import GreetingView, BlogView

urlpatterns = [
    url(r'^$', BlogView.as_view()),
    url(r'^google/$', RedirectView.as_view(url="http://www.google.com.hk"), name='google'),
    #url(r'^$', login_required(GreetingView.as_view())),

]
