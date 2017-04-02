from django.db import models

class expense(models.Model):
    category=models.CharField(max_length=100)
    amount=models.IntegerField()
    Description=models.TextField(max_length=300)
    user=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.amount
    
class category(models.Model):
    value=models.CharField(max_length=100 ,unique=True)
    
    def __str__(self):
        return self.value


