def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board, player):
    combos = [
        [0,1,2], [3,4,5], [6,7,8],  #rows
        [0,3,6], [1,4,7], [2,5,8],  #columns
        [0,4,8], [2,4,6]            #diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in combos)

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

# ---------- MINIMAX FUNCTIONS ----------
def minimax(board, depth, is_maximizing, computer, user):
    if check_winner(board, computer):
        return 1
    elif check_winner(board, user):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                temp = board[i]
                board[i] = computer
                score = minimax(board, depth + 1, False, computer, user)
                board[i] = temp
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                temp = board[i]
                board[i] = user
                score = minimax(board, depth + 1, True, computer, user)
                board[i] = temp
                best_score = min(score, best_score)
        return best_score

def best_move(board, computer, user):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] not in ['X', 'O']:
            temp = board[i]
            board[i] = computer
            score = minimax(board, 0, False, computer, user)
            board[i] = temp
            if score > best_score:
                best_score = score
                move = i
    return move

# ---------- GAME MODES ----------
def player_vs_player(score):
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input.")
            continue

        move = int(move) - 1
        if board[move] in ['X', 'O']:
            print("That spot is taken.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            score[current_player] += 1
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            score["Draw"] += 1
            break

        current_player = 'O' if current_player == 'X' else 'X'

def player_vs_computer(score):
    board = ['1','2','3','4','5','6','7','8','9']
    user = 'X'
    computer = 'O'

    while True:
        print_board(board)
        move = input("Your turn (1-9): ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input.")
            continue

        move = int(move) - 1
        if board[move] in ['X', 'O']:
            print("That spot is taken.")
            continue

        board[move] = user

        if check_winner(board, user):
            print_board(board)
            print("🎉 You win!")
            score["You"] += 1
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            score["Draw"] += 1
            break

        comp_move = best_move(board, computer, user)
        board[comp_move] = computer
        print(f"Computer chose position {comp_move + 1}")

        if check_winner(board, computer):
            print_board(board)
            print("💻 Computer wins!")
            score["Computer"] += 1
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            score["Draw"] += 1
            break

# ---------- MAIN GAME LOOP ----------
def tic_tac_toe():
    print("🎮 Welcome to Tic-Tac-Toe!")

    while True:
        print("\nChoose Game Mode:")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        mode = input("Enter your choice (1 or 2): ")

        if mode == '1':
            score = {"X": 0, "O": 0, "Draw": 0}
            game_func = player_vs_player
        elif mode == '2':
            score = {"You": 0, "Computer": 0, "Draw": 0}
            game_func = player_vs_computer
        else:
            print("Invalid choice. Try again.")
            continue

        while True:
            game_func(score)

            # Show scoreboard
            print("\n📊 Scoreboard:")
            for player, s in score.items():
                print(f"{player}: {s}")

            again = input("\nPlay again? (y/n): ").lower()
            if again != 'y':
                print("Thanks for playing! 👋")
                return

# Run the game
tic_tac_toe()
