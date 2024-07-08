from django.utils.translation import gettext_lazy as _
from django.db import models


class Parentesco(models.TextChoices):
    FATHER = 'FATHER', _("pai")
    MOTHER = 'MOTHER', _('mãe')
    PARTNER = 'PARTNER', _('conjuge')
    OTHER = 'OTHER', _('outro')
