from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='index'),
    path(
        'encuesta/<int:pk>',
        views.QuestionDetailView.as_view(),
        name='detail'
    ),
    path('vote', views.vote, name='vote'),
    path(
        '<int:pk>/results',
        views.QuestionResultView.as_view(),
        name='results'
    ),
]
