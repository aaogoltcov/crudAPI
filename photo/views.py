from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.models import Profile
from .serializer import PhotoSerializer, PhotoSerializerEmpty, CommentSerializer
from .models import Photo


class PhotoList(generics.ListAPIView):
    """
    PHOTO LIST - получение информации о фото пользователя, который авторизирован
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def list(self, request, *args, **kwargs):
        return Response(PhotoSerializer(self.get_queryset().filter(owner_id=self.request.user.id), many=True).data)


class PhotoCreate(generics.CreateAPIView):
    """
    PHOTO CREATE - размещение фотографии и комментария пользователем, который авторизирован
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        print(self.request.user)
        print(Profile.objects.filter(user_id=self.request.user.id).all())
        if Profile.objects.filter(user_id=self.request.user.id).values('photo_can_upload')[0]['photo_can_upload']:
            return PhotoSerializer
        else:
            return PhotoSerializerEmpty


class CommentUpdate(generics.UpdateAPIView):
    """
    COMMENT UPDATE - обновление комментария к фото
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = CommentSerializer


class PhotoDelete(generics.DestroyAPIView):
    """
    PHOTO DELETE - удаление фото
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializerEmpty

    def perform_destroy(self, instance):
        instance.delete_flag = True
        instance.save()
