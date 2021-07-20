from rest_framework import serializers
from .models import Photo
import imagehash as imagehash
from PIL import Image


class PhotoSerializer(serializers.ModelSerializer):
    """
    Сериализация фото в случае, если есть разрешение на добавление фото
    """
    class Meta:
        model = Photo
        fields = [
            'photo',
            'comment',
            'date',
            'delete_flag',
        ]
        read_only_fields = [
            'date',
            'delete_flag',
        ]
        extra_kwargs = {
            'date': {'read_only': True},
            'delete_flag': {'read_only': True}
        }

    def validate(self, data):
        """
        Валидация загружаемой фото
        """
        if imagehash.colorhash(Image.open(data['photo'])).__hash__() % 2 != 0:
            raise serializers.ValidationError({"Error": "You can't upload this picture"})
        return data


class PhotoSerializerEmpty(serializers.ModelSerializer):
    """
    Сериализация фото в случае, если разрешение на добавление фото отсуствует
    """
    class Meta:
        model = Photo
        fields = [
            'photo',
            'comment',
            'date',
            'delete_flag',
        ]
        read_only_fields = [
            'photo',
            'comment',
            'date',
        ]
        # exclude = [
        #     'photo',
        #     'comment',
        #     'date',
        #     'owner',
        # ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Обновление комментария
    """
    class Meta:
        model = Photo
        fields = [
            'comment',
        ]
        read_only_fields = [
            'photo',
            'date',
        ]
