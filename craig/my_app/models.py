from django.db import models

# Create your models here.

class Search(models.Model):
    search = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    created = models.DateTimeField()

    def __str__(self):
        return '{}, in {}'.format(self.search, self.area)

    class Meta:
        verbose_name_plural = 'Searches'
