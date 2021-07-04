from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]  # constant
MOVE_POS = 20  # future_proof_code
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :
    def __init__(self) :
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]    #initialising after creating snakes so list is ot empty

    def create_snake(self) :
        for i in range(3) :
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(STARTING_POS[i])
            self.segments.append(new_turtle)

    #extend snake on eating food
    def extend(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        last_seg_pos = self.segments[-1].position()   #position method returns the position of turtle in (x,y) tuple
        new_turtle.goto(last_seg_pos)
        self.segments.append(new_turtle)


    def move(self) :
        for seg_num in range(len(self.segments) - 1, 0,
                             -1) :  # range(start,stop,step)  //including start and excluding stop
            # get 2nd last segment position
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            # change the pos of current segment
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_POS)

    def up(self) :
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self) :
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self) :
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self) :
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
