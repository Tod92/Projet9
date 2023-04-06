from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
# Pillow pour manipulation images
from PIL import Image
# blog/models.py



class Photo(models.Model):

    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        image.save(self.image.path)
    # Surcharge de la fonction save pour y ajouter la resize systematiquement
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

class Ticket(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=30)
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
