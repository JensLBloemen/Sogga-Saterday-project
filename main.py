from classes.game import Game


def main(name):
    game = Game(name)
    game.run()


if __name__ == '__main__':
    name = input("Enter your name: ")
    main(name)