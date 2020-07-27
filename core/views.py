from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Question
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector


class Home(View):
	form_class = SearchForm

	def get(self, request):
		form = self.form_class
		questions = Question.objects.all()
		if 'search' in request.GET:
			form = self.form_class(request.GET)
			if form.is_valid():
				query = form.cleaned_data['search']
				questions = questions.annotate(search=SearchVector('title', 'body')).filter(search=query)
		return render(request, 'core/home.html', {'questions':questions, 'form':form})


class QuestionDetail(View):
	def get(self, request, id, slug):
		question = get_object_or_404(Question, id=id, slug=slug)
		return render(request, 'core/detail.html', {'question':question})
