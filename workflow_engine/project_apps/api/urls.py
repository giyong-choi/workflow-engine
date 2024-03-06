from django.urls import path

from project_apps.api.views import *

urlpatterns = [
    path('workflow', WorkflowAPIView.as_view()),
    path('workflow/<uuid:workflow_uuid>', WorkflowAPIView.as_view()),
    path('workflow/list', WorkflowListReadAPIView.as_view()),
    path('workflow/execute/<uuid:workflow_uuid>', WorkflowExecuteAPIView.as_view()),
    path('workflow/scheduling', SchedulingAPIView.as_view()),
    path('workflow/scheduling/<uuid:scheduling_uuid>', SchedulingAPIView.as_view()),
    path('workflow/scheduling/list', SchedulingListReadAPIView.as_view()),
    path('workflow/scheduling/list/<uuid:workflow_uuid>', WorkflowSchedulingListReadAPIView.as_view()),
    path('workflow/scheduling/execute/<uuid:scheduling_uuid>', SchedulingExecuteAPIView.as_view()),
]
