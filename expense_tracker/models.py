from django.db import models

class ExpenseModel(models.Model):
    CHOICE_CATEGORY = [
        ('F','FOOD'),
        ('T','TRAVEL'),
        ('E',"ENTERTAINMENT"),
        ('S',"SPORTS"),
        ('O',"OTHERS")
    ]
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=2,choices=CHOICE_CATEGORY)

    def __str__(self):
        return f"{self.title} - {self.amount}"
    


# Create your models here.
