from django.urls import path, include

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='index'),
    path(
        'encuesta/<int:pk>',
        views.QuestionDetailView.as_view(),
        name='detail'
    ),
    path('vote', views.QuestionVoteView.as_view(), name='vote'),
    path(
        '<int:pk>/results',
        views.QuestionResultView.as_view(),
        name='results'
    ),
    path('api/', include('apps.polls.api.urls')),
]
