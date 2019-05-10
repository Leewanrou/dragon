from django.shortcuts import render
from game.models import Game
from game.forms import GameForm

# Create your views here.



def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return render(request, 'main/main.html')

def game(request):
    '''
    Render the game page
    '''
    
#     records = Game.objects.all()
#     if not records.exists():
#         record = Game.objects.create(totalNum=0, answerNum=0)
#     else:
#         record = records.first()
#     
#     guess = int(request.POST.get('guess'))
#     cave = random.randint(1, 2)
#     if guess == cave:
#         record.answerNum += 1
#     else:
#         print('dead')
#     record.totalNum += 1
#     record.save()
    
    return render(request, 'main/game.html')

