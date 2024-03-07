from django.db import models

# Create your models here.
class Author(models.Model):
    # Author's first name
    first_name = models.CharField(max_length=100)
    # Author's last name
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Item(models.Model):
    code = models.CharField(max_length=16, unique=True, )
    name = models.CharField(max_length=512, )
    name_en = models.CharField(max_length=512, )