from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
# Pillow pour manipulation images
from PIL import Image




class Photo(models.Model):

    image = models.ImageField(blank=True)
    caption = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        if self.image:
            image = Image.open(self.image)
            image.thumbnail(self.IMAGE_MAX_SIZE)
            # Sauvegarde de l’image redimensionnée dans le système de fichiers
            # ce n’est pas la méthode save() du modèle !
            image.save(self.image.path)
    # Surcharge de la fonction save pour y ajouter la resize systematiquement
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
    # Surchage pour suppression du fichier du serveur media
    def delete(self, *args, **kwargs):
        #os.remove(self.image.path)
        super().delete(*args, **kwargs)

class AvatarPic(Photo):
    IMAGE_MAX_SIZE = (200, 200)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class TicketPic(Photo):
    IMAGE_MAX_SIZE = (400, 400)


class Ticket(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=30)
    photo = models.ForeignKey(TicketPic, null=True, on_delete=models.SET_NULL, blank=True)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def get_review(self):
        """
        Retourne la review associée si trouvée
        """
        return Review.objects.filter(ticket=self)
        
    def update_photo(self, photo_object):
        """
        Demande à la photo actuelle de se supprimer et mets à jour avec la
        photo envoyée en argument.
        """
        if self.photo:
            self.photo.delete()
        photo_object.save()
        self.photo = photo_object
        self.save()
        return None


class Review(models.Model):
    ONE_TO_FIVE_RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=ONE_TO_FIVE_RATING_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
        )
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
