class Library:

    def __init__(self, game):
        self.game = game
        self.lendDict = {}

    def show(self):
        print("Following games are available")
        for game in self.game:
            print(game)

    def lend(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("You can now borrow")
        else:
            print(f"Book has been issued to {self.lendDict[book]}. You can't Borrow")


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
            print("Correspondinbg Number to book you want to borrow")
            game.show()
            name=input("Book you want to borrow:")
            user=input("Enter your name: ")
            game.lend(user, name)
            Library.initilization()

        elif a==3:
            game.add()
            Library.initilization()

        elif a==4:
            pass

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
