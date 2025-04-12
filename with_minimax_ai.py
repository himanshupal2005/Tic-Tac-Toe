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
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

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

def tic_tac_toe():
    board = ['1','2','3','4','5','6','7','8','9']
    user = 'X'
    computer = 'O'

    while True:
        print_board(board)

        # User Move
        move = input("Your turn (1-9): ")
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Choose a number between 1 and 9.")
            continue

        move = int(move) - 1
        if board[move] in ['X', 'O']:
            print("That spot is already taken.")
            continue

        board[move] = user

        if check_winner(board, user):
            print_board(board)
            print("🎉 You win!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer Move (using Minimax)
        comp_move = best_move(board, computer, user)
        board[comp_move] = computer
        print(f"Computer chose position {comp_move + 1}")

        if check_winner(board, computer):
            print_board(board)
            print("💻 Computer wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
tic_tac_toe()
