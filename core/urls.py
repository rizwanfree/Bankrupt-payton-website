from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.searchByName, name='byname'),
    path('state/', views.statePage, name='states'),
    #path('bystate/<str:sname>', views.searchByState, name='bystate'),
    path('casedetails/<slug>/', views.caseDetails, name='caseDetails'),
    #path('contact/', views.contact_us, name='contact')
]
