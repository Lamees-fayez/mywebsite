from django.urls import path, include

from. import views
app_name='pages'
urlpatterns=[
    path('first',views.first, name='first'),
    path('second',views.second, name='second'),
    path('login',views.login, name='login'),
]