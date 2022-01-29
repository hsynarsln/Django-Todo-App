from django.db import models
from django.forms import CharField


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    PRIORITY = (
        ('3', 'Low'),
        ('2', 'Medium'),
        ('1', 'High')
    )
    priority = models.CharField(max_length=50, choices=PRIORITY, default='3')
    isDone = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #! aşağıdaki iki yöntem ile de kullanabiliyoruz
        # return "{} {}".format(self.first_name, self.last_name)
        return f"{self.title}"
