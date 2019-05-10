from django.db import models

# Create your models here.
class Game(models.Model):
    totalNum = models.IntegerField()  # 總共遊玩次數
    answerNum = models.IntegerField()  # 總共答對次數

    def __str__(self):
        return str(self.totalNum)
    
