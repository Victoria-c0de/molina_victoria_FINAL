from django.db import models

# Create your models here.
class Inscrito(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    )


    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=20)
    observacion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.institucion.nombre}"

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre