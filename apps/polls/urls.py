from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='index'),
    path('<int:pk>', views.QuestionDetailView.as_view(), name='detail'),
]
