import tkinter as tk
import random

CELL_SIZE = 20
GRID_WIDTH = 25
GRID_HEIGHT = 15
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("贪吃蛇")
        self.canvas = tk.Canvas(self.window, width=GRID_WIDTH * CELL_SIZE,
                                height=GRID_HEIGHT * CELL_SIZE, bg=BG_COLOR)
        self.canvas.pack()
        self.score = 0
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.food = self.create_food()
        self.direction = "Right"
        self.game_running = True
        self.bind_keys()
        self.draw()
        self.update_game()

    def create_food(self):
        while True:
            food = (random.randint(0, GRID_WIDTH - 1),
                    random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x * CELL_SIZE, y * CELL_SIZE,
                (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                fill=SNAKE_COLOR, outline=""
            )
        fx, fy = self.food
        self.canvas.create_oval(
            fx * CELL_SIZE, fy * CELL_SIZE,
            (fx + 1) * CELL_SIZE, (fy + 1) * CELL_SIZE,
            fill=FOOD_COLOR, outline=""
        )
        self.canvas.create_text(10, 10, anchor="nw",
                                 text=f"得分: {self.score}",
                                 fill="white", font=("Arial", 12))

    def update_game(self):
        if not self.game_running:
            return
        self.move_snake()
        if self.check_collision():
            self.game_over()
            return
        self.draw()
        delay = max(50, 200 - self.score * 5)
        self.window.after(delay, self.update_game)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1
        elif self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1
        new_head = (head_x, head_y)
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True
        if self.snake[0] in self.snake[1:]:
            return True
        return False

    def game_over(self):
        self.game_running = False
        self.canvas.delete("all")
        self.canvas.create_text(
            GRID_WIDTH * CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2,
            text=f"游戏结束!\n最终得分: {self.score}\n按 R 键重新开始",
            fill="white", font=("Arial", 16), justify="center"
        )

    def restart(self):
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.game_running = True
        self.update_game()

    def bind_keys(self):
        self.window.bind("<Up>", lambda e: self.change_direction("Up"))
        self.window.bind("<Down>", lambda e: self.change_direction("Down"))
        self.window.bind("<Left>", lambda e: self.change_direction("Left"))
        self.window.bind("<Right>", lambda e: self.change_direction("Right"))
        self.window.bind("w", lambda e: self.change_direction("Up"))
        self.window.bind("s", lambda e: self.change_direction("Down"))
        self.window.bind("a", lambda e: self.change_direction("Left"))
        self.window.bind("d", lambda e: self.change_direction("Right"))
        self.window.bind("r", lambda e: self.restart())
        self.window.bind("R", lambda e: self.restart())

    def change_direction(self, new_direction):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if opposites.get(new_direction) != self.direction:
            self.direction = new_direction

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
