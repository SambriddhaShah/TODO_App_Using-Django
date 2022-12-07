from django.db import models

# Create your models here.
class Todo(models.Model):
    title= models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    date_posted=models.DateField(auto_now_add=True)
    is_complete=models.BooleanField()

    class Meta:
        db_table='TODO'
        verbose_name='TODOS'

    def __str__(self):
        return self.title