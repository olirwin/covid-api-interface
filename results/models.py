from django.db import models


class Region(models.Model) :

    name = models.CharField("Nom", max_length = 128)
    code = models.CharField("Code", max_length = 4)

    def __str__(self) :
        return f"{self.name} ({self.code})"

    class Meta :
        verbose_name_plural = "Régions"
        verbose_name = "Région"
