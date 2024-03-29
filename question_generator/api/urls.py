from django.urls import path

from api.views import (generate_question_controller,
                       rate_candidate_answer_controller)

app_name = 'api'

urlpatterns = [
    path('api/v1/generate_question/', generate_question_controller),
    path('api/v1/rate_candidate_answer/', rate_candidate_answer_controller),
]
