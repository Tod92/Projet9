from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

from feed.models import AvatarPic
# Create your models here.


class User(AbstractUser):

    profile_photo = models.ForeignKey(AvatarPic,
                                      null=True,
                                      on_delete=models.SET_NULL,
                                      blank=True,
                                      related_name='profile_pic')

    following = models.ManyToManyField('self',
                                       # limit_choices_to={'role': CREATOR},
                                       blank=True,
                                       symmetrical=False,
                                       verbose_name='Suivre',
                                       through='UserFollows',
                                       )


# Table intermediaire pour la relation ManyToManyField
class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='follows')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followed_by')
    time_created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     # ensures we don't get multiple UserFollows instances
    #     # for unique user-user_followed pairs
    #     unique_together = ('user', 'followed_user')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'followed_user'],
                                    name="unique_followers")
                      ]

        # ordering = ["-created"]
