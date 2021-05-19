from django.urls import path
from .views import *

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),

    #Photos
    path('photos/<int:pk>', PhotosDetailView.as_view(), name='photo'),
    path('photos/new', PhotosAddView.as_view(), name='photo_new'),
    path('photos/<int:pk>/del', PhotosDeleteView.as_view(), name='photo_del'),
    path('photos/<int:pk>/edit', PhotosEditView.as_view(), name='photo_edit'),

    #Categories
    path('cate/<int:pk>', CategoryDetailView.as_view(), name='cate'),
    path('cate/new', CategoryAddView.as_view(), name='cate_new'),
]
