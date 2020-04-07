from django.urls import path
from . import views
from main.views import ArticleListView

urlpatterns = [
    path('', views.index),
    path('home/', views.index),
    path('home', views.index),
    path('blog/', views.ArticleListView.as_view(), name='blog.html'),
    path('blog', views.ArticleListView.as_view(), name='blog.html'),
    path('admin/', views.volevi)
]