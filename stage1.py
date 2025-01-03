import random

domino = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
          [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
          [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
          [3, 3], [3, 4], [3, 5], [3, 6],
          [4, 4], [4, 5], [4, 6],
          [5, 5], [5, 6],
          [6, 6]]

stock_pieces = []
computer_pieces = []
player_pieces = []
start_piece = []
def random_stock_pieces():

    for i in range(14):
        random_domino = random.choice(domino)
        stock_pieces.append(random_domino)
        domino.remove(random_domino)
    return f"Stock pieces: {stock_pieces}"


def random_first_move():
    first_move = random.randint(0,1)
    if first_move == 1:
        return True
    else:
        return False
def random_computer_pieces():
    for i in range(7):
        random_domino = random.choice(domino)
        computer_pieces.append(random_domino)
        domino.remove(random_domino)
    return f"Computer pieces: {computer_pieces}"


def random_player_pieces():
    for i in range(7):
        random_domino_player = random.choice(domino)
        player_pieces.append(random_domino_player)
        domino.remove(random_domino_player)

    maximum = max(player_pieces)
    return maximum

def random_computer_pieces():
    for i in range(7):
        random_domino_computer = random.choice(domino)
        computer_pieces.append(random_domino_computer)
        domino.remove(random_domino_computer)

    maximum = max(computer_pieces)
    return maximum


def random_domino_snake(maximum_computer, maximum_player):
    if maximum_computer > maximum_player:
        start_piece.append(maximum_computer)
        computer_pieces.remove(maximum_computer)
    else:
        start_piece.append(maximum_player)
        player_pieces.remove(maximum_player)

    return start_piece

maximum_computer = random_computer_pieces()
maximum_player = random_player_pieces()
domino_snake = random_domino_snake(maximum_computer, maximum_player)
print(random_stock_pieces())
print(f"Computer pieces: {computer_pieces}")
print(f"Player pieces: {player_pieces}")
print(f"Domino snake: {start_piece}")

if len(computer_pieces) < len(player_pieces):
    print("Status: player")
else:
    print("Status: computer")

