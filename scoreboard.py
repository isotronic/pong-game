from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 250)
        self.write(self.left_score, align="center", font=("Courier", 30, "normal"))
        self.goto(50, 250)
        self.write(self.right_score, align="center", font=("Courier", 30, "normal"))

    def add_point(self, player):
        if player == "left":
            self.left_score += 1
        elif player == "right":
            self.right_score += 1
        self.update_scoreboard()

