from django.urls import include, path

from . import views

endpoints = [
    path(
        'question/<int:pk>/results',
        views.QuestionResultAPIView.as_view(),
        name='results_api'
    )
]

urlpatterns = [
    path('v1/', include(endpoints)),
]
