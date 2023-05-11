from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Levels(models.Model):
    LEVELS=(
        (1,'level 1'),
        (2,'level 2'),
        (3,'level 3')
    )
    level=models.CharField(max_length=10,choices=LEVELS)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.category}-{self.level}")

class Questions(models.Model):
    question=models.CharField(max_length=200)
    level=models.ForeignKey(Levels,on_delete=models.CASCADE)

    def __str__(self):
        return(self.question)
    
class Answers(models.Model):
    answer=models.CharField(max_length=50)
    is_correct=models.BooleanField(default=False)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)

    def __str__(self):
        return(self.answer)
    