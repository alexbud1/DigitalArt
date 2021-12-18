from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		#####All the fields required to fill form
		fields = ("email", 'access_to_data', "first_name", "last_name")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#####deleting password confirmation which is default field
		del self.fields['password2']