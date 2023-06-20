from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return (self.title)

class Level(models.Model):
    LEVELS = (
        (1, 'level 1'),
        (2, 'level 2'),
        (3, 'level 3'),
        (4, 'level 4'),
        (5, 'level 5')
    )
    level=models.IntegerField(max_length=10,choices=LEVELS,default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # time=models.CharField(max_length=10)

    def __str__(self):
        return(f"{self.category}-{self.level}")



class Question(models.Model):
    text=models.CharField(max_length=300)
    level=models.ForeignKey(Level,on_delete=models.CASCADE)

    def __str__(self):
        return (self.text)

class Answer(models.Model):
    text=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return (self.text)
    
# class user_progress(models.Model):
#     is_completed=models.BooleanField(default=False)
#     level=models.ForeignKey(Level,on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.level}"


