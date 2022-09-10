from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls
    path('', views.customIndexV3, name='Custom Index'),
    # ex: /polls/2
    path('<int:question_id>', views.detail, name='Details'),
    # ex: /polls/2/custom-results
    path('<int:question_id>/custom-results', views.results, name='Custom Results'),
    # ex: /polls/2/custom-votes
    path('<int:question_id>/custom-votes', views.vote, name='Custom Voting'),
]