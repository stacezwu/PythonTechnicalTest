from django.db import models

class Bond(models.Model):
    isin = models.CharField(max_length=12)
    size = models.IntegerField(default=0)
    currency = models.CharField(max_length=3)
    maturity = models.DateField()
    lei = models.CharField(max_length=20)
    legal_name = models.CharField(max_length=100)

    def __str__(self):
        return self.isin