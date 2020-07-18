from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('<int:id>/<slug:slug>/', views.QuestionDetail.as_view(), name='detail'),
]