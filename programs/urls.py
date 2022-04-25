from django.urls import path, include
from . import views

app_name = 'programs'

urlpatterns = [

    path('support/', views.supportList, name="support"),
    path('special/', views.specialEvents),
    path('faithnet/', views.testpdf),
    path('classes/', views.classList),
    path('<int:pk>/', views.programDetail, name="program"),
    path('', views.landing),

]