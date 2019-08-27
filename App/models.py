from django.db import models


# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=32, db_column='name', unique=True)
    p_age = models.IntegerField(db_column='age')
    p_sex = models.BooleanField(db_column="sex")
    p_hobby = models.CharField(max_length=32, null=True, db_column='hobby')

    @classmethod
    def create(cls, p_name, p_age=100, p_sex=True, p_hobby="game"):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex, p_hobby=p_hobby)

    class Meta:
        db_table = 'People'
        verbose_name = 'ChinaPeople'
