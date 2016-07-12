from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

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
