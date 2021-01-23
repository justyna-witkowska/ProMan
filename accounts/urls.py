from django.urls import path
from viewer.views import View_to_change
from .views import SignUpView

app_name = 'accounts'
urlpatterns = [
    # path('signup', View_to_change, name='signup'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('logout', View_to_change, name='logout'),
    path('login', View_to_change, name='login'),
    path('password_change', View_to_change, name='change-password')
]
