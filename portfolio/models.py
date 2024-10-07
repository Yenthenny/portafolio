from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images") # para trabajar con imagenes se debe instalar esta paquete -- pip install Pillow
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title

#NUEVO MODELO DEL MASTER VERA
class Curso(models.Model):
  institucion_del_curso = models.CharField(max_length=225)
  descripcion_curso = models.TextField()
  fecha_curso = models.DateField()
  numero_horas = models.PositiveIntegerField()

  def _str_(self):
    return f'{self.descripcion_curso} - {self.institucion_del_curso}'