from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls
    path('', views.customIndexV3, name='Custom Index'),
    # ex: /polls/v1/2
    path('v1/<int:question_id>', views.detail, name='Details'),
    # ex: /polls/v2/2
    path('v2/<int:question_id>', views.detailV2NotFound, name='Details raise 404'),
    # ex: /polls/v3/2
    path('v3<int:question_id>', views.detailV3NotFound, name='Details raise 404'),
    # ex: /polls/2/custom-results
    path('<int:question_id>/custom-results', views.results, name='Custom Results'),
    # ex: /polls/2/custom-votes
    path('<int:question_id>/custom-votes', views.vote, name='Custom Voting'),
]