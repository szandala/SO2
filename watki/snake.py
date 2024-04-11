import curses
import time
import threading
import random


COLUMNS = 50
ROWS = 25

class Board:

    def __init__(self):
        self.score = 0
        self.field = [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

        self.snake = [ (int(ROWS/2), int(COLUMNS/2)) ]
        self.direction = 1

        self.foods = {}
        self.game_over = False

        self.lock_food = threading.Lock() # mutex
        self.condition_move = threading.Condition()

    def __str__(self):
        score = f"Score: {self.score}"
        area = "#" * COLUMNS + score + "\n"
        for row in self.field:
            area += "#"
            for slot in row:
                area += slot
            area += "#\n"
        area += "#" * COLUMNS
        return area

    def refresh(self):
        self.field = [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]
        for r,c in self.snake:
            self.field[r][c] = str(self.direction)
        for (r,c), typ in self.foods.items():
            self.field[r][c] = typ

    def controller(self, new_direction):
        #   1
        #4     2
        #   3
        with self.condition_move:
            if not abs(self.direction-new_direction) == 2:
                self.direction = new_direction
                self.condition_move.wait()

    def add_food(self, food_coord, typ):
        self.lock_food.acquire()
        self.foods[food_coord] = typ
        self.lock_food.release()

    def eat_food(self):
        if self.snake[0] in self.foods:
            self.score += 1
            self.snake.insert(0, self.snake[0])

            with self.lock_food:
                del self.foods[self.snake[0]]


    def move(self):
        r,c = self.snake[0]
        with self.condition_move:
            if self.direction == 1:
                r -= 1
            elif self.direction == 2:
                c += 1
            elif self.direction == 3:
                r += 1
            else:
                c -= 1
            self.snake.insert(0, (r,c))
            self.eat_food()
            self.snake.pop()
            print("notifying")
            self.condition_move.notify()

def controller(window, board):
    while not board.game_over:
        char = window.getch()
        if char == curses.KEY_UP:
            board.controller(1)
        elif char == curses.KEY_RIGHT:
            board.controller(2)
        elif char == curses.KEY_DOWN:
            board.controller(3)
        elif char == curses.KEY_LEFT:
            board.controller(4)


def spawn_food(board, typ="%"):
    while not board.game_over:
        c = random.randint(1, COLUMNS-2)
        r = random.randint(1, ROWS-2)
        board.add_food((r,c), typ)
        time.sleep(2)


def start(window):
    board = Board()

    control = threading.Thread(target=controller, args=(window, board))
    control.start()

    waiter = threading.Thread(target=spawn_food, args=(board, ))
    waiter.start()

    waiter2 = threading.Thread(target=spawn_food, args=(board, ")"))
    waiter2.start()

    while not board.game_over:
        window.clear()
        window.insstr(0, 0, str(board))
        window.refresh()
        time.sleep(0.2)

        board.move()
        board.refresh()

    control.join()
    waiter.join()
    waiter2.join()


if __name__ == "__main__":
    curses.wrapper(start)
