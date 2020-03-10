

from django.contrib import admin
from django.urls import path, include
from Candidate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('candidate/',include('Candidate.urls',namespace="Candidate")),
    path('',views.home,name='home'),
    path('logout/', views.user_logout, name='logout'),
]


