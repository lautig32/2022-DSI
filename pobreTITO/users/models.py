from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, null=True, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    cuil_cuim = models.CharField(verbose_name="CUIM/CUIL", max_length=15, null=True, blank=True)
    phone = models.CharField(_('teléfono'), max_length=20, blank=True, null=True)
    mobile = models.CharField(_('celular'), max_length=20, blank=True, null=True)
    description = models.TextField(_("descripción"), blank=True)
    
    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        if not self.password:
            self.set_password(str(self.cuil_cuim))
        super(User, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
            self.save()
        else:
            super(User, self).delete(using, keep_parents)

    def __str__(self):
        return "%s - %s" % (self.cuil_cuim, self.get_full_name())

