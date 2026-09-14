import random
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

SIZE = 15
EMPTY = 0
BLACK = 1
WHITE = 2

def check_win(board, x, y, player):
    directions = [(1,0),(0,1),(1,1),(1,-1)]
    for dx, dy in directions:
        line = [(x,y)]
        nx, ny = x+dx, y+dy
        while 0 <= nx < SIZE and 0 <= ny < SIZE and board[ny][nx] == player:
            line.append((nx,ny))
            nx += dx
            ny += dy
        nx, ny = x-dx, y-dy
        while 0 <= nx < SIZE and 0 <= ny < SIZE and board[ny][nx] == player:
            line.insert(0,(nx,ny))
            nx -= dx
            ny -= dy
        if len(line) >= 5:
            return line
    return None

def evaluate_pos(board, x, y, player):
    score = 0
    directions = [(1,0),(0,1),(1,1),(1,-1)]
    for dx, dy in directions:
        count = 1
        open_ends = 0
        nx, ny = x+dx, y+dy
        while 0 <= nx < SIZE and 0 <= ny < SIZE and board[ny][nx] == player:
            count += 1
            nx += dx
            ny += dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE and board[ny][nx] == EMPTY:
            open_ends += 1
        nx, ny = x-dx, y-dy
        while 0 <= nx < SIZE and 0 <= ny < SIZE and board[ny][nx] == player:
            count += 1
            nx -= dx
            ny -= dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE and board[ny][nx] == EMPTY:
            open_ends += 1
        if count >= 5:
            score += 100000
        elif count == 4:
            if open_ends == 2: score += 10000
            elif open_ends == 1: score += 1000
        elif count == 3:
            if open_ends == 2: score += 1000
            elif open_ends == 1: score += 100
        elif count == 2:
            if open_ends == 2: score += 100
            elif open_ends == 1: score += 10
        elif count == 1:
            score += 1
    return score

def ai_move(board, ai_player, difficulty):
    opponent = BLACK if ai_player == WHITE else WHITE
    empty = [(x,y) for y in range(SIZE) for x in range(SIZE) if board[y][x] == EMPTY]
    if not empty:
        return None
    if difficulty == 'easy':
        if random.random() < 0.3:
            for x,y in empty:
                if check_win(board, x, y, ai_player):
                    return (x,y)
            for x,y in empty:
                if check_win(board, x, y, opponent):
                    return (x,y)
        return random.choice(empty)
    best_score = -1
    best_moves = []
    for x,y in empty:
        ai_score = evaluate_pos(board, x, y, ai_player)
        opp_score = evaluate_pos(board, x, y, opponent)
        if difficulty == 'normal':
            total = ai_score + opp_score * 0.8
        else:
            total = ai_score + opp_score * 1.2
        if total > best_score:
            best_score = total
            best_moves = [(x,y)]
        elif total == best_score:
            best_moves.append((x,y))
    return random.choice(best_moves)

def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data['board']
    x = data['x']
    y = data['y']
    player = data['player']
    mode = data.get('mode', 'pvp')
    difficulty = data.get('difficulty', 'normal')

    if not (0 <= x < SIZE and 0 <= y < SIZE):
        return jsonify({'error': 'Invalid position'}), 400
    if board[y][x] != EMPTY:
        return jsonify({'error': 'Cell not empty'}), 400

    board[y][x] = player
    win = check_win(board, x, y, player)
    if win:
        return jsonify({'board': board, 'ai': None, 'win': {'player': player, 'line': win}})
    if is_full(board):
        return jsonify({'board': board, 'ai': None, 'win': {'player': 0, 'line': None}})

    ai_info = None
    if mode == 'ai':
        ai_player = WHITE if player == BLACK else BLACK
        ai_pos = ai_move(board, ai_player, difficulty)
        if ai_pos:
            ax, ay = ai_pos
            board[ay][ax] = ai_player
            ai_info = {'x': ax, 'y': ay}
            win = check_win(board, ax, ay, ai_player)
            if win:
                return jsonify({'board': board, 'ai': ai_info, 'win': {'player': ai_player, 'line': win}})
            if is_full(board):
                return jsonify({'board': board, 'ai': ai_info, 'win': {'player': 0, 'line': None}})

    return jsonify({'board': board, 'ai': ai_info, 'win': None})

if __name__ == '__main__':
    app.run(debug=True)
