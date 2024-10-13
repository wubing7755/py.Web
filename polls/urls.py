from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/question_id/
    path("<int:question_id>/", views.details, name="detail"),
    # ex: /polls/question_id/results/
    path("<int:question_id>/results/",views.results, name="results"),
    # ex: /polls/question_id/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
