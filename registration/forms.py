# import form class from django
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, ChoiceField

# import GeeksModel from models.py
from people.models import Member

# create a ModelForm
class MemberForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Member
		fields = "__all__"
		widgets = {
				'name': TextInput(attrs={
					'class': "form-control",
					'style': 'max-width: 300px;',
					'placeholder': 'Name'
				}),
				'email': TextInput(attrs={
					'class': "form-control",
					'style': 'max-width: 300px;',
					'placeholder': 'Email'
				}),
			'phone': TextInput(attrs={
				'class': "form-control",
				'style': 'max-width: 300px;',
				'placeholder': 'Phone'
			}),

			}
