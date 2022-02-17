from django.urls import path, include
from . import views

app_name = "events"

urlpatterns = [
    path('<int:prg>/', views.filterEvents.as_view(), name="filtered"),
    path('calendar/', views.cal_view),
    path('', views.CalendarView.as_view(), name='events'),

]