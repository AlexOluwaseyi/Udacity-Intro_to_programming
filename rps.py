#!/usr/bin/env python3
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


import random
from colorama import Fore, Style, Back


moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def perror(message):
    print(Fore.RED + message + Style.RESET_ALL + Style.RESET_ALL)


class Player:
    """
    The Player class - The parent class
    All players inherit from this 'Player' class
    """
    def __init__(self, score=0):
        """
        Initializer for Player class
        Player score initialized to zero for all players
        """
        self.score = score
        self.my_moves = []
        self.op_moves = []

    def move(self):
        """
        Placeholder for move for all subclass
        Moves are defined in subclasses
        """
        pass

    def learn(self, my_move, their_move):
        """
        Function to help learn (keep track of) players moves
        """
        self.my_moves.append(my_move)
        self.op_moves.append(their_move)


def beats(one, two):
    """
    Function to check moves and return winners
    for each rounds
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RockPlayer(Player):
    """
    Defines a Random Player class
    Inherits from 'Player' class (subsclass)
    RandomPlayer moves are decided by random choices carried out
    by the random module
    """
    def __init__(self, name):
        """
        Initializer for RockPlayer class
        Name is initialized
        Inherits initializer from Player class (especially score)
        """
        super().__init__()
        self.name = name

    def move(self):
        """
        Player always plays 'rock'
        """
        return 'rock'


class RandomPlayer(Player):
    """
    Defines a Random Player class
    Inherits from 'Player' class (subsclass)
    RandomPlayer moves are decided by random choices carried out
    by the random module
    """
    def __init__(self, name):
        """
        Initializer for RandomPlayer class
        Name is initialized
        Inherits initializer from Player class (especially score)
        """
        super().__init__()
        self.name = name

    def move(self):
        """
        Function to make move
        Move is randomized among values in list 'moves' using the
        random module
        Return:
            A random choice from moves
        """
        return random.choice(moves)


class ReflectPlayer(Player):
    """
    Defines a Reflect Player class
    Reflect player plays the last game played by the human player
    Inherits from 'Player' class (subsclass)
    """
    def __init__(self, name):
        """
        Initializer for ReflectPlayer class
        Name is initialized
        Inherits initializer from Player class (especially score)
        """
        super().__init__()
        self.name = name

    def move(self):
        """
        Function to make move
        Reflects the opponent's last move and plays same move
        Uses the learn method to monitor and know opponent's moves
        Return:
            Opponents last move or a random move if opponent
            hasn't made a move yet
        """
        if len(self.op_moves) > 0:
            return self.op_moves[-1]
        else:
            return random.choice(moves)


class CyclePlayer(Player):
    """
    Defines a Cycle Player class
    Player cycles through the list of moves and plays the moves in turn
    Inherits from 'Player' class (subsclass)
    """
    def __init__(self, name):
        """
        Initializer for CyclePlayer class
        Name is initialized
        Inherits initializer from Player class (especially score)
        """
        super().__init__()
        self.name = name

    def move(self):
        """
        Function to make move
        Check own last move in the moves list and play next move
        Uses index() method to check the index of previous move,
        adds one to the index and return the item at index+1
        Also uses the modulo (%) operator to ensure that index does
        not exceed the lenght of the list 'moves'.
        Return:
            Next move in the list or a random move if CyclePlayer
            hasn't made a move yet
        """
        if len(self.op_moves) > 0:
            last_move = self.my_moves[-1]
            last_move_index = moves.index(last_move)
            next_move_index = (last_move_index + 1) % len(moves)
            next_move = moves[next_move_index]
            return next_move
        else:
            Cycle_move = random.choice(moves)
            self.my_moves.append(Cycle_move)
            return Cycle_move


class HumanPlayer(Player):
    """
    Defines a Human Player class
    Request for players moves from stdin using input()
    Inherits from 'Player' class (subsclass)
    """
    def __init__(self, name):
        """
        Initializer for HumanPlayer class
        Name is initialized and collected from the Game class
        Inherits initializer from Player class (especially score)
        """
        super().__init__()
        self.name = name

    def move(self, p_move=""):
        """
        Player's moves are collected using input() method.
        Moves are converted into lowercase using .lower() method
        while loop continues to ask player for input until a valid
        input is supplied.
        Return:
            p_name
        """
        while p_move not in moves:
            p_move = input("What's your move: ").lower()
        return p_move


class Game:
    """
    Defines the Game class
    The Rock, Paper, Scissors game core class
    """
    def __init__(self, p1, p2):
        """
        Initializer for game
        Players are initialized
        """
        self.p1 = p1
        self.p2 = p2

    def win_lose(self, move1, move2):
        """
        Defines the condition for winning or losing a round in the game
        Checks using the beats function.
        Increments the score of the winner by 1 based on results of
        comparison between the players' moves.
        """
        if beats(move1, move2):
            self.p1.score += 1
            print(
                f"{Fore.BLACK}{Back.GREEN}"
                f"{self.p1.name}: {self.p1.score}\t"
                f"{Style.RESET_ALL}"
                f"{self.p2.name}: {self.p2.score}"
            )
        elif beats(move2, move1):
            self.p2.score += 1
            print(
                f"{self.p1.name}: {self.p1.score}\t"
                f"{Fore.BLACK}{Back.GREEN}"
                f"{self.p2.name}: {self.p2.score}"
                f"{Style.RESET_ALL}"
            )
        else:
            print("That's a tie")
            print(
                f"{self.p1.name}: {self.p1.score}\t"
                f"{self.p2.name}: {self.p2.score}"
            )

    def play_round(self):
        """
        Function to play a round of game and check winner
        Collects players' moves and compares using the win_lose() function
        Also collects and record players' moves using the learn() method
        """
        print(
            f"{self.p1.name}: {self.p1.score}\t"
            f"{self.p2.name}: {self.p2.score}"
        )
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(
            f"{self.p1.name}: {move1}\t"
            f"{self.p2.name}: {move2}"
            )
        self.win_lose(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        """
        Function to play game
        Human player choose the type of games:
            'Best of three' or 'Best of five'
        Keeps track of the number of rounds
        """
        rounds = 0
        print()
        print("Game starts!")
        print(f"{self.p1.name}\tvs\t{self.p2.name}")
        print()
        print("What kind of game do you want to play?")
        print("1. Best of 3\n2. Best of 5")
        while True:
            try:
                game_type = int(input("Enter 1 or 2: "))
                if (game_type == 1) or (game_type == 3):
                    game = 3
                    print("Best of 3")
                    print()
                    break
                elif (game_type == 2) or (game_type == 5):
                    game = 5
                    print("Best of 5")
                    print()
                    break
                else:
                    perror("Invalid choice.")
            except ValueError:
                perror("Invalid choice.")
        while self.p1.score < game and self.p2.score < game:
            rounds += 1
            print(f"Round {rounds}:")
            self.play_round()
            print()
        if self.p1.score == game:
            print(f"{self.p1.name} wins the game!")
            print(
                "Final score:\n"
                f"{Fore.BLACK}{Back.GREEN}"
                f"{self.p1.name}: {self.p1.score}\t"
                f"{Style.RESET_ALL}"
                f"{self.p2.name}: {self.p2.score}"
            )
        else:
            print(f"{self.p2.name} wins the game!")
            print(
                "Final score:\n"
                f"{self.p1.name}: {self.p1.score}\t"
                f"{Fore.BLACK}{Back.GREEN}"
                f"{self.p2.name}: {self.p2.score}"
                f"{Style.RESET_ALL}"
            )
        print("Game over!")


if __name__ == '__main__':
    p1 = RockPlayer("Computer")
    # p1 = RandomPlayer("Computer")
    # p1 = ReflectPlayer("Computer")
    # p1 = CyclePlayer("Computer")
    p2 = HumanPlayer(input("What's your name? ").title())
    game = Game(p1, p2)
    game.play_game()
