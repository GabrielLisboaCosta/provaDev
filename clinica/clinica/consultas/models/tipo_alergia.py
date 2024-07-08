from django.utils.translation import gettext_lazy as _
from django.db import models


class TipoAlergia(models.TextChoices):
    FOOD = 'FOOD', _("comida")
    DRUG = 'DRUG', _('medicamento')
    INSECT = 'INSECT', _('insetos')
    OTHER = 'OTHER', _('outros')
    