from engine import Game
from matplotlib import pyplot

n_games = 1000
n_shots = []
n_wins_1 = 0
n_wins_2 = 0

for i in range(n_games):
    game = Game(human1=False, human2=False)
    while not game.over:
        if game.player1_turn:
            game.basic_ai()
        else:
            game.basic_ai()
    n_shots.append(game.n_shots)
    if game.result == 1:
        n_wins_1 += 1
    elif game.result == 2:
        n_wins_2 += 1

print(n_wins_1)
print(n_wins_2)

values = []
for i in range(17,200):
    values.append(n_shots.count(i))

pyplot.bar(range(17,200),values)
pyplot.show()
