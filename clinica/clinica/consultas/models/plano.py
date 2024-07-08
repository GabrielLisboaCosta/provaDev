from django.utils.translation import gettext_lazy as _
from django.db import models


class Plano(models.TextChoices):
    UNIMED = 'UNIMED', _("Unimed")
    DOCTOR_CLIN = 'DOCTOR_CLIN', _('Doctor Clin')
    PUBLIC = 'PUBLIC', _('Publico')
    PRIVATE = 'PRIVATE', _('Particular')
