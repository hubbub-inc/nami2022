from django.urls import path, include
from .views import pdf_view, documents_home, loss_view, support_view

app_name = 'documents'

urlpatterns = [
    path('schizophrenia/', pdf_view),
    path('loss/', loss_view),
    path('support/', support_view),
    path('', documents_home),

]