from django.db import models
from django.urls import reverse

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_absolute_url(self):
        return reverse('first_app:musician_details', kwargs={'pk': self.pk})


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name ='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    
    RATING_CHOICES = [
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent"),
    ]
    num_stars = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name + " " + str(self.num_stars)
