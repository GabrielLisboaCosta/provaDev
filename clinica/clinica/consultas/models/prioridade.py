from django.utils.translation import gettext_lazy as _
from django.db import models


class Prioridade(models.TextChoices):
    LOW = 'LOW', _("baixa")
    MEDIUM = 'MEDIUM', _('media')
    HIGH = 'HIGH', _('alta')
    URGENCY = 'URGENCY', _('urgencia')
