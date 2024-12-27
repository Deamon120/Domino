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

def player_choices(number):
    if number < 0:
        player_choice = player_pieces[abs(number)-1]
        if start_piece[0][0] == player_pieces[abs(number)-1][1]:
            start_piece.insert(0, player_choice)
        elif start_piece[0][0] != player_pieces[abs(number)-1][1] and start_piece[0][0] == player_pieces[abs(number)-1][0]:
            start_piece.insert(0, player_choice[::-1])
        else:
            return "Illegal move. Please try again."
        player_pieces.remove(player_choice)
    elif number == 0:
        random_stock = random.choice(stock_pieces)
        player_pieces.append(random_stock)
        stock_pieces.remove(random_stock)
        return random_stock
    else:
        player_choice = player_pieces[abs(number)-1]
        if start_piece[-1][1] == player_pieces[abs(number)-1][0]:
            start_piece.append(player_choice)
        elif start_piece[-1][1] != player_pieces[abs(number)-1][0] and start_piece[-1][1] == player_pieces[abs(number)-1][1]:
            start_piece.append(player_choice[::-1])
        else:
            return "Illegal move. Please try again."
        player_pieces.remove(player_choice)
    return player_choice

def sorted_computer_domino():
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    for piece in computer_pieces:
        if piece[0] == 0:
            count_0 += 1
        elif piece[1] == 0:
            count_0 += 1
        if piece[0] == 1:
            count_1 += 1
        elif piece[1] == 1:
            count_1 += 1
        if piece[0] == 2:
            count_2 += 1
        elif piece[1] == 2:
            count_2 += 1
        if piece[0] == 3:
            count_3 += 1
        elif piece[1] == 3:
            count_3 += 1
        if piece[0] == 4:
            count_4 += 1
        elif piece[1] == 4:
            count_4 += 1
        if piece[0] == 5:
            count_5 += 1
        elif piece[1] == 5:
            count_5 += 1
        if piece[0] == 6:
            count_6 += 1
        elif piece[1] == 6:
            count_6 += 1
    for piece in domino_snake:
        if piece[0] == 0:
            count_0 += 1
        elif piece[1] == 0:
            count_0 += 1
        if piece[0] == 1:
            count_1 += 1
        elif piece[1] == 1:
            count_1 += 1
        if piece[0] == 2:
            count_2 += 1
        elif piece[1] == 2:
            count_2 += 1
        if piece[0] == 3:
            count_3 += 1
        elif piece[1] == 3:
            count_3 += 1
        if piece[0] == 4:
            count_4 += 1
        elif piece[1] == 4:
            count_4 += 1
        if piece[0] == 5:
            count_5 += 1
        elif piece[1] == 5:
            count_5 += 1
        if piece[0] == 6:
            count_6 += 1
        elif piece[1] == 6:
            count_6 += 1
    weights = {0: count_0, 1: count_1, 2: count_2, 3: count_3, 4: count_4, 5: count_5, 6: count_6}
    sorted_domino = sorted(computer_pieces, key=lambda x: weights[x[0]] + weights[x[1]], reverse=True)
    return sorted_domino
def computer_choices():
        computer_domino = sorted_computer_domino()
        for piece in computer_domino:
            if start_piece[0][0] == piece[1]:
                start_piece.insert(0, piece)
                computer_pieces.remove(piece)
                break
            elif start_piece[0][0] != piece[1] and start_piece[0][0] == piece[0]:
                start_piece.insert(0, piece[::-1])
                computer_pieces.remove(piece)
                break
            elif start_piece[-1][1] == piece[0]:
                start_piece.append(piece)
                computer_pieces.remove(piece)
                break
            elif start_piece[-1][1] != piece[0] and start_piece[-1][1] == piece[1]:
                start_piece.append(piece[::-1])
                computer_pieces.remove(piece)
                break
        else:
            random_stock = random.choice(stock_pieces)
            computer_pieces.append(random_stock)
            stock_pieces.remove(random_stock)
            return random_stock

stock = random_stock_pieces()
maximum_computer = random_computer_pieces()
maximum_player = random_player_pieces()
domino_snake = random_domino_snake(maximum_computer, maximum_player)
status = ""

for i in range(70):
    print("=", end="")
print()
print(f"Stock size: {len(stock_pieces)}")
print(f"Computer pieces: {len(computer_pieces)}")
print()
print(start_piece[0])
print()
print("Your pieces:")
for i in range(len(player_pieces)):
    print(f"{i+1}:{player_pieces[i]}")
print()
if len(computer_pieces) < len(player_pieces):
    status = "Status: It's your turn to make a move. Enter your command."
    print(status)
else:
    status = "Status: Computer is about to make a move. Press Enter to continue..."
    print(status)
while len(computer_pieces) > 0 and len(player_pieces) > 0:
    if status == "Status: It's your turn to make a move. Enter your command.":
        player_input = input()
        try:
            value = int(player_input)
            if value > len(player_pieces) or value < -len(player_pieces):
                print("Invalid input. Please try again.")
                continue
            player_choices_function = player_choices(value)
            if player_choices_function == "Illegal move. Please try again.":
                print(player_choices_function)
                continue
        except ValueError:
            print("Invalid input. Please try again.")
            continue
    else:
        player_input = input().strip()
        if player_input == "":
            computer_choices()
        else:
            print("Invalid input. Please try again.")
            continue

    for i in range(70):
        print("=", end="")
    print()
    print(f"Stock size: {len(stock_pieces)}")
    print(f"Computer pieces: {len(computer_pieces)}")
    print()
    if len(start_piece) < 7:
        for piece in start_piece:
            print(piece, end="")
        print()
    else:
        print(f"{start_piece[0]} {start_piece[1]} {start_piece[2]}...{start_piece[-3]} {start_piece[-2]} {start_piece[-1]}")
    print()
    print("Your pieces:")
    for i in range(len(player_pieces)):
        print(f"{i + 1}:{player_pieces[i]}")
    print()
    if status == "Status: Computer is about to make a move. Press Enter to continue...":
        status = "Status: It's your turn to make a move. Enter your command."
    else:
        status = "Status: Computer is about to make a move. Press Enter to continue..."

    if len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        break
    if len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        break
    count = 0
    number = start_piece[0][0]
    for piece in start_piece:
        if piece[0] == number:
            count += 1
        if piece[1] == number:
            count += 1
    if start_piece[0][0] == start_piece[-1][1] and count == 8:
        print("Status: The game is over. It's a draw!")
        break
    if len(start_piece) == 0:
        print("Status: The game is over. It's a draw!")
        break
    print(status)
