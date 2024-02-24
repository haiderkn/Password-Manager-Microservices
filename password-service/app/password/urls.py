from django.urls import path
from .views import CredentialCreate, CredentialEdit, CredentialList


urlpatterns = [
    path('create/', CredentialCreate.as_view()),
    path('list/', CredentialList.as_view()),
    path('edit/<int:pk>/', CredentialEdit.as_view()),
    # path('edit/<pk:int>', CredentialEdit.as_view()),
]
