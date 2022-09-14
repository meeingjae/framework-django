from django.urls import path

from . import views

app_name = 'polls_app'
urlpatterns = [
    # ex: /polls
    path('', views.custom_index_v3, name='Custom Index'),
    # ex: /polls/v1/2
    path('v1/<int:question_id>', views.detail, name='Details'),
    # ex: /polls/v2/2
    path('v2/<int:question_id>', views.detail_v2_not_found, name='details_v2'),
    # ex: /polls/v3/2
    path('v3/<int:question_id>', views.detail_v3_not_found, name='details_v3'),
    # ex: /polls/2/custom-results
    path('<int:question_id>/results', views.results, name='result'),
    # ex: /polls/2/custom-votes
    path('<int:question_id>/votes', views.vote, name='voting'),

    path('', views.IndexView.as_view(), name='index_as_view'),
    path('<int:pk>', views.DetailView.as_view(), name='detail_as_view'),
    path('<int:pk>/results', views.ResultView.as_view(), name='result_as_view'),
]
