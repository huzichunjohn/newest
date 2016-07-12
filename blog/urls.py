from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from blog.views import GreetingView

urlpatterns = [
    url(r'^$', GreetingView.as_view()),
    #url(r'^$', login_required(GreetingView.as_view())),

]
