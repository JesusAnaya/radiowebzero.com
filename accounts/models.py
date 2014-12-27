from django.db import models
from django.contrib.auth.models import AbstractUser

WEEK_DAYS = (
    (0, 'Lunes'),
    (1, 'Martes'),
    (2, 'Miescoles'),
    (3, 'Jueves'),
    (4, 'Viernes'),
    (5, 'Sabado'),
    (6, 'Domingo'),
)

class User(AbstractUser):
    photo = models.ImageField(upload_to='accounts/photos/',
                                    blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    google_plus = models.URLField(blank=True, null=True)


class Hour(models.Model):
    user = models.ForeignKey(User)
    day = models.IntegerField(default=0, choices=WEEK_DAYS)
    time = models.TimeField()

    class Meta:
        verbose_name = u'Horario'
        verbose_name_plural = u'Horarios'