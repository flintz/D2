from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.Charfield(max_length=128, verbose_name=u"Title")
    desc = models.TextField(verbose_name=u"Text News")
    datetimestamp = models.DateTimeField(auto_now=True, verbose_name=u"Date/Time")



