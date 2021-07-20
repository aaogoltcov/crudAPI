from django.contrib import admin
from django.urls import path, include
from photo.views import PhotoList, PhotoCreate, CommentUpdate, PhotoDelete
from user.views import UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', PhotoList.as_view()),
    path('create', PhotoCreate.as_view()),
    path('update/<int:pk>', CommentUpdate.as_view()),
    path('delete/<int:pk>', PhotoDelete.as_view()),
    path('register', UserCreate.as_view()),
    path('auth/', include('rest_framework.urls')),
]