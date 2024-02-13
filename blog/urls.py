from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name='blog-index'),
    #path('', views.PostListView.as_view(), name='blog-index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='blog-detail'),
]
