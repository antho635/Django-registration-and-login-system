from django.urls import path
from .views import home, profile, RegisterView, home_test, view_profile

urlpatterns = [
    path('', home, name='users-home'),
    path('test/', home_test, name='test-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('myprofile/', view_profile, name='view_profile'),
    path('profile/', profile, name='users-profile'),
]
