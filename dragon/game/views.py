import random
from django.shortcuts import render
from game.models import Game


# Create your views here.
def game(request):
    if request.method == "GET": 
        return render(request, 'game/game.html')
    
    records = Game.objects.all()
    if not records.exists():
        record = Game.objects.create(totalNum=0, answerNum=0)
    else:
        record = records.first()
        
    if request.method == "POST":  
        guess = int(request.POST.get('guess'))
        cave = random.randint(1, 2)

        if guess == cave:
            record.answerNum += 1
            record.totalNum += 1
            record.save()
            text = '恭喜你,噴火龍和你分享金銀財寶!'

        else:
            text = '噴火龍一口把你吃了'
            record.totalNum += 1
            record.save()
    return render(request, "game/game.html", {'text':text, 'record':record})


def dele(request):
    Game.objects.all().delete()
    renew = Game.objects.create(totalNum=0, answerNum=0)
    return render(request, 'game/game.html', {'zero':renew})
