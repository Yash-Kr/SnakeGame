from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Score(Turtle) :
    def __init__(self) :
        super().__init__()
        self.score = -1
        self.goto(0, 270)
        self.color("white")
        self.ht()

    def update_score(self) :
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER !", move=False, align=ALIGNMENT, font=FONT)