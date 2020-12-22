from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.FloatField()
    is_married = models.BooleanField(default=False)
    description = models.TextField()

    dob = models.DateField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = (
            '-salary',
            'name',
        )
