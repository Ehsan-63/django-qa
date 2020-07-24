from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Question
from .forms import SearchForm
from django.db.models import Q


class Home(View):
	form_class = SearchForm

	def get(self, request):
		form = self.form_class
		questions = Question.objects.all()
		search = request.GET.get('search')
		if search:
			questions = questions.filter( Q(title__icontains=search) | Q(body__icontains=search) )
		return render(request, 'core/home.html', {'questions':questions, 'form':form})


class QuestionDetail(View):
	def get(self, request, id, slug):
		question = get_object_or_404(Question, id=id, slug=slug)
		return render(request, 'core/detail.html', {'question':question})
