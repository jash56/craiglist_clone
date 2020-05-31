from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'
