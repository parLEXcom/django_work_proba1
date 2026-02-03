from django.db import models

class Uchastok(models.Model):
    name= models.CharField(max_length=20, default='значение_по_умолчанию')

    def __str__(self):
        return self.name


class Station_namber(models.Model):
    title = models.CharField(max_length=50)
    data = models.DateField()
    namber_1 = models.IntegerField()
    namber_2 = models.IntegerField()
    namber_3 = models.IntegerField()
    namber_4 = models.IntegerField()
    namber_5 = models.IntegerField()
    uchastoc = models.ForeignKey(Uchastok, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


