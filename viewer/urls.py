from django.urls import path, include
from viewer.views import View_to_change, MockMembersListView

urlpatterns = [
    path('', MockMembersListView.as_view(), name='mock_member_list_view'),
    path('delete_team', View_to_change, name='team_delete'),
    path('change_manager', View_to_change, name='manager_change'),
    path('end_task/<int:pk>', View_to_change, name='task_end'),
    path('add_member', View_to_change, name='member_add'),
    path('delete_member/<int:pk>', View_to_change, name='member_delete'),
    path('modify_user_tasks/<int:pk>', View_to_change, name='tasks_modify'),
    path('delete_task/<int:pk>', View_to_change, name='task_delete'),
    path('add_task', View_to_change, name='task_add'),
]
