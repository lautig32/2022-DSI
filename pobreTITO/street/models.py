from django.db import models

# Create your models here.

class Street(models.Model):
    code = models.IntegerField('codigo', blank=False, null=True, unique=True)
    name = models.CharField('calle', max_length=30, blank=False, null=True, unique=True)

    class Meta:
        verbose_name = "calle"
        verbose_name_plural = "calles"

    def __str__(self):
        return "%s" % (self.name)