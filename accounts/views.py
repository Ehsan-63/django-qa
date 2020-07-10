from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages


class UserRegister(View):
	form_class = UserRegistrationForm
	template_name = 'accounts/register.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
			user.save()
			messages.success(request, 'you registered successfully', 'info')
			return redirect('core:home')
		return render(request, self.template_name, {'form':form})