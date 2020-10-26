from django.db import models

# Create your models here.

class Collection(models.Model):
    desease_term = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.desease_term

class Sample(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    donor_count = models.IntegerField()
    material_type = models.CharField(max_length=250)
    last_updated = models.DateField()

    def __str__(self):
        return str(self.id)

