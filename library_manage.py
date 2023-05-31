class Library:

    def __init__(self, game):
        self.game = game

    def show(self):
        print("Following games are available")
        for game in self.game:
            print(game)

    def add(self):
        print("Enter the game")
        new = input()
        self.game.append(new)

    def initilization():
        a = int(input())
        if a==1:
            game.show()
            Library.initilization()
        elif a==2:
            game.add()
            Library.initilization()
        elif a==5:
            return 0    
        else:
            print('Unknown Command')





#initial books:
game_list=['zelda', 'pokemon', 'call of duty', 'yakuza 6']
game = Library(game_list)


print('Welcome to VideoGame Library')
print('1. Show Games')
print('2. Lend Games')
print('3. Add Games')
print('4. Return Games')
print('5. EXIT')

Library.initilization()
