from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.PollListView.as_view(), name='index'),
]
