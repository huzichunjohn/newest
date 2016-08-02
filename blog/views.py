from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import View, FormView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.template.loader import get_template, render_to_string
from django.template import Context
from django.core.mail import EmailMessage
from .models import Blog, Author
from .forms import ContactForm, AuthorForm
import logging
logger = logging.getLogger(__name__)

class GreetingView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    greeting = "Good Day"

    def get(self, request):
        logger.warning("an error")
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

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
	context = super(AboutView, self).get_context_data(**kwargs)
        now = timezone.localtime(timezone.now())
	if now.weekday() < 5 and 8 < now.hour < 18:
	    context['open'] = True
	else:
	    context['open'] = False
	return context

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
	contact_name = form.cleaned_data['contact_name']
	contact_email = form.cleaned_data['contact_email']
	form_content = form.cleaned_data['content']
	
	context = {
	    'contact_name': contact_name,
	    'contact_email': contact_email,
	    'form_content': form_content
	}
	content = render_to_string('contact_template.txt', context)
	
	email = EmailMessage(
	    'new contact',
	    content,
	    from_email='Dont reply<do_not_reply@domain.com>',
	    to=['to_email'],
	    headers = {'Reply-To': contact_email}
	)
	email.send()
	return super(ContactView, self).form_valid(form)

class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    template_name = 'blog/detail.html'

    def get_object(self):
	object = super(AuthorDetailView, self).get_object()
	object.last_accessed = timezone.now()
	object.save()
	return object

class AuthorListView(ListView):
    context_object_name = 'authors'
    queryset = Author.objects.all()
    template_name = 'blog/list.html'

class AjaxableResponseMixin(object):
    def form_invalid(self, form):
	response = super(AjaxableResponseMixin, self).form_invalid(form)
	if self.request.is_ajax():
	    return JsonResponse(form.errors, status=400)
	else:
	    return response

    def form_valid(self, form):
	response = super(AjaxableResponseMixin, self).form_valid(form)
	if self.request.is_ajax():
	    data = {
		'pk': self.object.pk,
	    }
	    return JsonResponse(data)
	else:
	    return response

class AuthorCreate(AjaxableResponseMixin, CreateView):
    model = Author
    form_class = AuthorForm

    def form_valid(self, form):
	#form.instance.created_by = self.request.user
	return super(AuthorCreate,self).form_valid(form)

class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
