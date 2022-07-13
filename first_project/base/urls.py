from django.urls import path
from .views import Customlogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Customlogin.as_view()),


]
