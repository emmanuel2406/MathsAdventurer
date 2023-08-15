"""MathsAdventurer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("test", views.test, name="test"),
    path("competitions", views.competitions, name="competitions"),
    path("resources", views.topics, name="topics"),
    path("resources/<int:topic_id>", views.resources, name="resources"),
    path("profile", views.profile, name="profile"),
    path("status_update", views.status_update, name="status_update"),
    path("watchlist_update", views.watchlist_update, name="watchlist_update"),
    path("new_milestone", views.new_milestone, name="new_milestone"),
    path("archive", views.archive, name="archive"),
    path("calendar", views.calendar, name="calendar"),
    path("get_events", views.get_events, name="get_events")
]
