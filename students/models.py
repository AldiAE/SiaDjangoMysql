from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Student(models.Model):
    class Prodi(models.TextChoices):
        Teknik_Informatika = 'IF', _('Teknik Informatika')
        Teknik_Elektro = 'EL', _('Teknik Elektro')
        Teknik_Mesin = 'MS', _('Teknik Mesin')
        Teknik_Industri = 'TI', _('Teknik Industri')
        Teknik_Lingkungan = 'LI', _('Teknik Lingkungan')
        pass

    nim = models.CharField(max_length=8, unique=True)
    nama = models.CharField(max_length=255)
    prodi = models.CharField(max_length=30, choices=Prodi.choices, default=Prodi.Teknik_Informatika)
    angkatan = models.IntegerField(default=2019)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.nim, self.nama, self.prodi, self.angkatan)
        pass
    pass


class MataKuliah(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    matkul = models.CharField(max_length=30)
