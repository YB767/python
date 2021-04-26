from turtle import Turtle
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self, complete_count):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.update_scoreboard(complete_count)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def update_scoreboard(self, complete_count):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {complete_count + 1}", align="center", font=FONT)