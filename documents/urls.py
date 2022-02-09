from django.urls import path, include
from .views import pdf_view, documents_home

app_name = 'documents'

urlpatterns = [
    path('schizophrenia/', pdf_view),
    path('', documents_home),

]