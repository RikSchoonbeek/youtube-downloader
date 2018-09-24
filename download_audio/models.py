from django.db import models


class AudioFile(models.Model):
    download_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='media/user_downloads/%Y/%m/%d/')
    url = models.ForeignKey(to="YouTubeURL", on_delete=models.CASCADE)
    quality = models.IntegerField()


class YouTubeURL(models.Model):
    url = models.URLField()
