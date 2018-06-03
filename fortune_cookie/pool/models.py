from django.db import models

class SeedFortune(models.Model):

    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "seed_fortune"
        verbose_name = "Seed Fortune"
        verbose_name_plural = "Seed Fortunes"

    def __str__(self):
       return self.description

