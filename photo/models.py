import django
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Photo(models.Model):
    """
    Модель фото с id, фотографией, комментарием и датой загрузки
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos')
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(default=django.utils.timezone.now)
    delete_flag = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.id, self.owner)

    class Meta:
        ordering = ['date']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
