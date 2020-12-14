from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Chart(models.Model):
    my_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Half', 'Half'),
    )
    date = models.DateField()
    clean_diet = models.CharField(max_length=5, choices=my_choices)
    coding = models.CharField(max_length=5, choices=my_choices)
    reading = models.CharField(max_length=5, choices=my_choices)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    wakeup_early = models.CharField(max_length=5, choices=my_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
