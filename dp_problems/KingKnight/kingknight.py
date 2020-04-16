def howMany(size, start, end, numMoves):
    board = [[0]*size for i in range(size)]
    i = 0
    while i < size
        j = 0
        while j < size:
            board[i][j] = get_num_moves_to_end([i, j], end)

def get_num_moves_to_end(position, end):
    if 

def get_all_can_go_to(position, size):
    legal_moves = []
    LEFT = False
    RIGHT = False
    UP = False
    DOWN = False
    if position[0] - 1 > -1:
        legal_moves.append([position[0]-1, position[1]])
        DOWN = True
    if position[1] - 1 > -1:
        legal_moves.append([position[0], position[1]-1])
        LEFT = True
    if position[0] + 1 < size:
        legal_moves.append([position[0]+1, position[1]])
        UP = True
    if position[1] + 1 < size:
        legal_moves.append([position[0], position[1]+1])
        RIGHT = True

    if DOWN and RIGHT:
        legal_moves.append([position[0]-1, position[1]+1])
    if DOWN and LEFT:
        legal_moves.append([position[0]-1, position[1]-1])
    if UP and RIGHT:
        legal_moves.append([position[0]+1, position[1]+1])
    if UP and LEFT:
        legal_moves.append([position[0]+1, position[1]-1])

    if UP and position[1] - 2 > -1:
        legal_moves.append([position[0]+1, position[1]-2])
    if DOWN and position[1] - 2 > -1:
        legal_moves.append([position[0]-1, position[1]-2])
    if LEFT and position[0] - 2 > -1:
        legal_moves.append([position[0]-2, position[1]-1])
    if LEFT and position[0] + 2 < size:
        legal_moves.append([position[0]+2, position[1]-1])

    if UP and position[1] + 2 < size:
        legal_moves.append([position[0]+1, position[1]+2])
    if DOWN and position[1] + 2 < size:
        legal_moves.append([position[0]-1, position[1]+2])
    if RIGHT and position[0] - 2 > -1:
        legal_moves.append([position[0]-2, position[1]+1])
    if RIGHT and position[0] + 2 < size:
        legal_moves.append([position[0]+2, position[1]+1])
     
    return legal_moves

def make_distance_grid(end, size):
    grid = [[0]*size for i in range(size)]
    curr_moves = set(get_all_can_go_to(end, size))
    future_moves = set()
    while True:
        i = 1
        for move in curr_moves:
            if grid[move[0]][move[1]] != 0:
                continue
            grid[move[0]][move[1]] = i
            future_moves.update(set(get_all_can_go_to(move, size)))
        curr_moves = future_moves
     #i'm up to checking for exit conditions
        future_moves = set()
        i += 1


    



assert len(get_all_can_go_to([0,0], 2)) == 3
assert len(get_all_can_go_to([1,0], 2)) == 3
assert len(get_all_can_go_to([0,1], 2)) == 3
assert len(get_all_can_go_to([1,1], 2)) == 3
assert len(get_all_can_go_to([8,10], 20)) == 16
