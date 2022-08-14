from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        '''Displays ScoreBoard'''
        super().__init__()
        self.penup()
        with open("D:\Projects\Python\Snake\data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.score = 0
        self.color("white")
        self.goto(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= "center", font=("Arial"))
        self.hideturtle()

    def collision(self):
        '''Adds Point'''
        self.clear()
        self.score += 1 
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= "center", font=("Arial"))

    def reset(self):
        '''Updates Highscore'''
        if self.score > self.high_score:
            with open("D:\Projects\Python\Snake\data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Resets Scoreboard'''
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= "center", font=("Arial"))
        