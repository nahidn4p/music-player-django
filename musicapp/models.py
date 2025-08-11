from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    audio_file = models.FileField(upload_to='audio_files/')
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    lyrics = models.CharField(max_length=5000, null=True, blank=True)
    duration = models.DurationField()
    

    def __str__(self):
        return f"{self.title} by {self.artist}"