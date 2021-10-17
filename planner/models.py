from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustomSettings(models.Model):  # noqa: D101

    TIME_INTERVAL = [
        [15, 15],
        [30, 30],
        [60, 60],
    ]

    company_name = models.CharField(
        _('Company name'),
        max_length=255,
        blank=True,
        null=True,
    )
    time_interval = models.IntegerField(
        _('Time Interval'),
        choices=TIME_INTERVAL,
        default=15,
    )
