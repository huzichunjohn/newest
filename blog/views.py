from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog

class GreetingView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    greeting = "Good Day"

    def get(self, request):
	return HttpResponse(self.greeting)

class RegisterView(View):
    form_class = UserCreationForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
	return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
	form = self.form_class(request.POST)
	if form.is_valid():
            form.save()
	    return HttpResponseRedirect(reverse('register_done'))
	return render(request, self.template_name, {'form': form})	

class RegisterDoneView(View):
    def get(self, request):
	return HttpResponse("success.")

class BlogView(LoginRequiredMixin, TemplateView):

    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
	context = super(BlogView, self).get_context_data(**kwargs)
	context['latest_blogs'] = Blog.objects.all()[:5]
	return context 
