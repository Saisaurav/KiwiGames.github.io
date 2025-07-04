import itertools

def rotate(board):
    # Rotates the board 90 degrees clockwise
    return (
        board[6], board[3], board[0],
        board[7], board[4], board[1],
        board[8], board[5], board[2]
    )

def reflect(board):
    # Reflects the board horizontally
    return (
        board[2], board[1], board[0],
        board[5], board[4], board[3],
        board[8], board[7], board[6]
    )

def canonical(board):
    # Returns the canonical (minimal) form of the board under all symmetries
    boards = [board]
    b = board
    for _ in range(3):
        b = rotate(b)
        boards.append(b)
    b = reflect(board)
    boards.append(b)
    for _ in range(3):
        b = rotate(b)
        boards.append(b)
    return min(boards)

def generate_unique_boards(num_O, num_X):
    # Generates all unique boards with num_O O's and num_X X's
    empty = 9 - num_O - num_X
    all_boards = set()
    for positions in itertools.permutations([1]*num_O + [-1]*num_X + [0]*empty, 9):
        can = canonical(positions)
        all_boards.add(can)
    return all_boards

def make_weights(board, weight):
    # Assigns the given weight to empty cells, 0 elsewhere
    return [weight if x == 0 else 0 for x in board]

if __name__ == "__main__":
    # Example: generate all unique boards for move 3 (1 O, 1 X)
    num_O = 3
    num_X = 3
    weight = 1  # Set your desired weight for this move

    boards = generate_unique_boards(num_O, num_X)
    boards_dict = {board: make_weights(board, weight) for board in boards}

    # Print as Python dictionary
    print("{")
    for k, v in boards_dict.items():
        print(f"    {k}: {v},")
    print("}")