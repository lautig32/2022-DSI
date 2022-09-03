from django.db import models

from street.models import Street
from users.models import User

from datetime import *


class Type(models.Model):
    name = models.CharField("nombre", max_length=100, blank=False, unique=True, null=False)
    description = models.TextField("descripción", blank=True, null=True)
    image = models.ImageField("imagen representativa", upload_to='tipos_reclamos', null=True, blank=False)
    is_active = models.BooleanField(verbose_name="activo", default=True)

    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"

    def __str__(self):
        return self.name


class Reason(models.Model):
    name = models.CharField("nombre", max_length=100, blank=False, unique=True, null=False)
    description = models.TextField("descripción", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="activo", default=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='tipo', related_name='reason_type', null=True,blank=False)

    objects = models.manager

    class Meta:
        verbose_name = "motivo"
        verbose_name_plural = "motivos"

    def __str__(self):
        return self.name


class ClaimRegister(models.Model):
    number_phone = models.CharField("Telefono", max_length=20,null=False,blank=True,default='')
    description = models.TextField("Descripción", null=True, blank=True)
    reason = models.ForeignKey(Reason, on_delete=models.PROTECT, verbose_name='motivo',
                               related_name='ClaimRegister_reason', null=True, blank=False)
    street_location = models.ForeignKey(Street, on_delete=models.PROTECT, verbose_name="domicilio",
                                        related_name="ClaimRegister_street_location", null=True, blank=False)
    number_street = models.IntegerField("numero domicilio", blank=False, null=True)
    street_location_a = models.ForeignKey(Street, on_delete=models.PROTECT, verbose_name="entre calle uno",
                                          related_name="ClaimRegister_street_location_a", null=True, blank=True)
    street_location_b = models.ForeignKey(Street, on_delete=models.PROTECT, verbose_name="entre calle dos",
                                          related_name="ClaimRegister_street_location_b", null=True, blank=True)
    citizen = models.ForeignKey(User, verbose_name="ciudadano", related_name="NoteClaim_citizen",
                                on_delete=models.PROTECT, null=True, blank=True)
    date_register_claim = models.DateTimeField(verbose_name="Fecha de inicio", default=datetime.now, auto_now=False,
                                               editable=False, blank=False)
    date_modified_claim = models.DateTimeField(verbose_name="Fecha de modificacion", auto_now=True, editable=True,
                                               blank=True)
    user_last_change = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Usuario que registro la ultima modificacion",
                                        related_name="user_last_change", null=True, blank=False)

    objects = models.manager

    class StateLocal(models.TextChoices):
        received = "RC", "Recibido"
        assigned = "AS", "Asignado"
        in_action = "EE", "En ejecución"
        complete = "CP", "Completado"

    state_local = models.CharField("Estado", max_length=15, choices=StateLocal.choices, default=StateLocal.assigned)
    
    RECEPTION_RECEPTIONIST = (
        ("CALL", "llamada"),
        ("WHAT", "whatsApp"),
    )

    class Reception(models.TextChoices):
        whatsapp = "WHAT", "whatsApp"
        web = "WEB", "web"

    reception = models.CharField("recepción", max_length=15, choices=Reception.choices, default=Reception.web)

    class Meta:
        verbose_name = "reclamo"
        verbose_name_plural = "reclamos"

    def __str__(self):
        return "Numero de reclamo: %d | Estado: %s" % (self.id, self.get_state_local_display())


class NoteClaim(models.Model):
    claim = models.ForeignKey(ClaimRegister, on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="autor", related_name="NoteClaim_author", on_delete=models.PROTECT)
    date = models.DateTimeField('fecha', auto_now=True, editable=False)
    note = models.TextField('nota', blank=False)

    class Meta:
        verbose_name = 'nota'
        verbose_name_plural = 'notas'

    def __str__(self):
        return self.note


class ImageClaim(models.Model):
    claim = models.ForeignKey(ClaimRegister, on_delete=models.CASCADE)
    note = models.TextField('nota', blank=True, null=True)
    image = models.ImageField("imagen", upload_to='', null=False, blank=False)

    class Meta:
        verbose_name = 'imagen'
        verbose_name_plural = 'imágenes'

    def __str__(self):
        return self.note