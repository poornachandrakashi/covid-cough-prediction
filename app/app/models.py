from django.db import models


class Response(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    fever = models.BooleanField(verbose_name='Have you been experiencing a fever?')
    travel = models.BooleanField(verbose_name='Have you recently traveled internationally?')
    cough = models.FileField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ",".join(str(i) for i in (self.name, self.city, self.age))
