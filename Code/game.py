import turtle
class PingPong:
    score_a, score_b = 0,0
    def __init__(self, height, width, color):
        self.wn = turtle.Screen()
        self.wn.title("Ping Pong")
        self.wn.bgcolor(color)
        self.wn.setup(width=width, height=height)
        self.wn.tracer(0)

    def game_object(self, shape, pos, color, wid, ln, step_x, step_y):
        self.object = turtle.Turtle()
        self.object.speed(0)
        self.object.shape(shape)
        self.object.color(color)
        self.object.shapesize(stretch_wid=wid, stretch_len=ln)
        self.object.penup()
        self.object.goto(pos,0)
        self.object.dx = step_x
        self.object.dy = step_y
        return self.object
    
    def object_movement(self, obj, dist, key):
        self.wn.listen()
        self.wn.onkeypress(lambda: obj.sety(obj.ycor()+dist),key)

    def print_score(self, color, pos):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color(color)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, pos)
        self.pen.write("Player A: {} Player B: {}".format(self.score_a, self.score_b), align="center", font=("Courier", 20, "normal"))

    def play(self, ball, left_paddle, right_paddle):
        while True:
            self.wn.update()
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            if(ball.ycor()>290):
                ball.sety(290)
                ball.dy*=(-1)

            if(ball.ycor()<-290):
                ball.sety(-290)
                ball.dy*=(-1)

            if(ball.xcor()>390):
                ball.setx(390)
                ball.dx*=(-1)
                self.score_a+=1
                self.pen.clear()
                self.pen.write("Player A: {} Player B: {}".format(self.score_a, self.score_b), align="center", font=("Courier", 20, "normal"))
            
            if(ball.xcor()<-390):
                ball.setx(-390)
                ball.dx*=(-1)
                self.score_b+=1
                self.pen.clear()
                self.pen.write("Player A: {} Player B: {}".format(self.score_a, self.score_b), align="center", font=("Courier", 20, "normal"))

            if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<right_paddle.ycor()+40 and ball.ycor()>right_paddle.ycor()-40):
                ball.setx(340)
                ball.dx*=(-1)
            
            if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<left_paddle.ycor()+40 and ball.ycor()>left_paddle.ycor()-40):
                ball.setx(-340)
                ball.dx*=(-1)

game = PingPong(600, 800, "black")
left_paddle = game.game_object("square", -350, "white", 5, 1, 0, 0)
right_paddle = game.game_object("square", 350, "white", 5, 1, 0, 0)
ball = game.game_object("circle", 0, "white", 1, -1, 0.15, -0.15)
game.object_movement(left_paddle, 20, "q")
game.object_movement(left_paddle, -20, "a")
game.object_movement(right_paddle, 20, "Up")
game.object_movement(right_paddle, -20, "Down")
game.print_score("white", 260)
game.play(ball, left_paddle, right_paddle)