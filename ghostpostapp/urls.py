from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('like/<int:post_id>/', views.like_view),
    path('dislike/<int:post_id>/', views.dislike_view),
    path('post_details/<int:id>', views.post_details, name='post_details'),
    path('form/', views.add_post, name='form'),
    path('boast/', views.boast_views, name='boast'),
    path('roast/', views.roast_views, name='roast')
]
