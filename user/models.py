from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Расширение пользовательской модели User для настройки правила "можно / нельзя загружать фото"
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_can_upload = models.BooleanField(default=True, verbose_name='Может загружать фото')

    def __str__(self):
        return "%s" % self.user

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
