from django.db import models

# Create your models here.


class Item(models.Model):
    """
    creates table Item, that has 2 headers: name and done
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
