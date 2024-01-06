# pulchihd@raspberrypi:~ $ sudo apt-get install python3-opencv
# pulchihd@raspberrypi:~ $ pip install chess
# pulchihd@raspberrypi:~ $ sudo apt-get install stockfish
import cv2 as cv
import chess
import chess.engine

# pulchihd@raspberrypi:~ $ which stockfish
path = '/usr/games/stockfish'
engine = chess.engine.SimpleEngine.popen_uci(path)

board = chess.Board()
game = True
while game:
    print(board)

    try:
        print("White to play, please enter a move using the UCI protocol.")
        user_input = input("Move: ")
        move = chess.Move.from_uci(user_input)
        if move in board.legal_moves:
            if len(board.legal_moves) < 1:
                print("Game over")
                break
            board.push(move) 
        else:
            print("Illegal move, try again")
            continue
    except Exception as e:
        print("An error occurred:", e)
        continue

    try:
        limit = chess.engine.Limit(time=1.0)
        best_move = engine.play(board, limit=limit)
        board.push(chess.Move.from_uci(str(best_move.move)))
    except Exception as e:
        print("An error occurred:", e)
        print("ChessBot has resigned")
        break

engine.quit()