from django.urls import path
from .views import UserRegistrationView

app_name = 'user'

urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='register'),

]