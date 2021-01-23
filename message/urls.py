from django.urls import path
from viewer.views import View_to_change

urlpatterns = [
    path('', View_to_change, name='messages_all'),
    path('id/<int:pk>', View_to_change, name='message_id'),
    path('new/', View_to_change, name='new_message')
]
