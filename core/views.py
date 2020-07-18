from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Question



class Home(View):
	def get(self, request):
		questions = Question.objects.all()
		return render(request, 'core/home.html', {'questions':questions})


class QuestionDetail(View):
	def get(self, request, id, slug):
		question = get_object_or_404(Question, id=id, slug=slug)
		return render(request, 'core/detail.html', {'question':question})
