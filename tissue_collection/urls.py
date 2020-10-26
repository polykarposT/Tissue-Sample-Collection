from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('samples/', views.samples, name='samples'),
    path('samples/<int:sample_id>/', views.sample, name='sample'),
    path('samples/<int:sample_id>/update/', views.update_sample, name='update_sample'),
    path('sample/<int:sample_id>/delete/', views.delete_sample, name='delete_sample'),
    path('collection/<int:collection_id>/', views.collection, name='collection'),
    path('collection/<int:collection_id>/create_sample/', views.create_sample, name='create_sample'),
    path('collection/<int:collection_id>/update/', views.update_collection, name='update_collection'),
    path('collection/<int:collection_id>/delete/', views.delete_collection, name='delete_collection'),
    path('create_collection/', views.create_collection, name='create_collection'),
]
