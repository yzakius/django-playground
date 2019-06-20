from django.contrib.auth.models import User
from django.db import models

DECK_CHOICES = (('B', 'Black'), ('W', 'White'), ('R', 'Red'), ('G', 'Green'), ('BU', 'Blue'))

class Plane(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_normal = models.BooleanField('Normal', default=False)
    is_apprentice = models.BooleanField('Apprentice', default=False)
    is_mage = models.BooleanField('Mage', default=False)
    is_planeswalker = models.BooleanField('Planeswalker', default=False)
    plane = models.ForeignKey(
        'core.plane',
        related_name='users',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


class Deck(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=2, default='B', choices=DECK_CHOICES)

    def __str__(self):
        return self.name
