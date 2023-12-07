from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.searchByName, name='byname'),
    path('state/', views.stateList, name='states'),
    path('bystate/<int:sid>', views.searchByState, name='bystate'),
    path('casedetails/<int:pk>/', views.caseDetails, name='caseDetails')
]
