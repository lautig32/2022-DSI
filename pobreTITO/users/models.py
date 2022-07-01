from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_upload_path.upload_path import auto_cleaned_path_stripped_uuid4


class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, null=True, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    cuil_cuim = models.CharField(verbose_name="CUIM/CUIL", max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(_('foto de perfil'), upload_to=auto_cleaned_path_stripped_uuid4, null=True,
                                        blank=True)
    phone = models.CharField(_('teléfono'), max_length=20, blank=True, null=True)
    mobile = models.CharField(_('celular'), max_length=20, blank=True, null=True)
    description = models.TextField(_("descripción"), blank=True)

    CITIZEN = 'Citizen'
    SUPERVISOR = 'Supervisor'
    RECEPTIONIST = 'Receptionist'
    ADMINISTRATOR = 'Administrator'

    USER_TYPE_CHOICES_SUPERVISOR = (
        (CITIZEN, 'Ciudadano'),
    )

    USER_TYPE_CHOICES_RECEPTIONIST = (
        (CITIZEN, 'Ciudadano'),
        (SUPERVISOR, 'Encargado'),
    )

    USER_TYPE_CHOICES_ADMINISTRATOR = (
        (CITIZEN, 'Ciudadano'),
        (SUPERVISOR, 'Encargado'),
        (RECEPTIONIST, 'Recepcionista'),
    )

    USER_TYPE_CHOICES = (
        (CITIZEN, 'Ciudadano'),
        (SUPERVISOR, 'Encargado'),
        (RECEPTIONIST, 'Recepcionista'),
        (ADMINISTRATOR, 'Administrador'),
    )

    user_type = models.CharField(_('tipo'), max_length=15, choices=USER_TYPE_CHOICES, default=CITIZEN)
    type = models.ForeignKey("claim.Type", verbose_name='tipo de reclamo', related_name='claim_reason_type', on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def profile_picture_short_tag(self):
        if self.profile_picture:
            url_image = self.profile_picture.url
            return format_html("""<img src='{}' width='40'"/>""", url_image)
        return "-"
    profile_picture_short_tag.short_description = _('foto de perfil')
    profile_picture_short_tag.allow_tags = True

    def profile_picture_medium_tag(self):
        if self.profile_picture:
            url_image = self.profile_picture.url
            return format_html("""<img src='{}' height='160'"/>""", url_image)
        return "-"
    profile_picture_medium_tag.short_description = _('foto de perfil')
    profile_picture_medium_tag.allow_tags = True

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

