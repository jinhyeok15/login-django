from django.urls import path

# views
from users import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
]
