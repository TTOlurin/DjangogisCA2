from django.urls import path

from .views import SignUpView
#url pattern for signup
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]