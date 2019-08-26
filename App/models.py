from django.db import models


# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=32, db_column='name', unique=True)
    p_age = models.IntegerField(db_column='age')
    p_sex = models.BooleanField(db_column="sex")

    class Meta:
        db_table = 'People'
        verbose_name = 'ChinaPeople'
