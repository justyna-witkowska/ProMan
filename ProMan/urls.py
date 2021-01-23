"""ProMan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from viewer.views import View_to_change, MockTeamsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MockTeamsListView.as_view(), name='dashboard'),
    path('team_delete/<int:pk>', View_to_change, name='team_delete'), # chyba powinno byc w aplikacji viewer
    path('add_team', View_to_change, name='team_add'),
    path('team/<int:pk>', include('viewer.urls')),
    path('message/', include('message.urls')),
    path('account/', include('accounts.urls')),
]
