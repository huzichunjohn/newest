from django import forms
from .models import Author

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
	required=True,
	widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
	super(ContactForm, self).__init__(*args, **kwargs)
	self.fields['contact_name'].label = "your name:"
	self.fields['contact_email'].label = "your email:"
	self.fields['content'].label = "what do you want to say?"

class AuthorForm(forms.ModelForm):
    class Meta:
	model = Author
	fields = ['name', 'last_accessed']
