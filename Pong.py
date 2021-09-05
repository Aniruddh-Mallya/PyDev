# Implementation of classic arcade game Pong
import simplegui
import random
# initialize globals - pos and vel encode vertical info for paddles
X = Y = 0
WIDTH = 1000
HEIGHT = 550
BANNER_HEIGHT = 100
BALL_RADIUS = 25
PAD_WIDTH = 16
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
DIRECTION = ["LEFT", "RIGHT"]
Z = (HEIGHT - PAD_HEIGHT) / HEIGHT 
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
left_paddle_vel = right_paddle_vel = 0
left_score = right_score = 0
direction = "LEFT" # by default
max_pace = 15 # customizable!
pace = 0
# initialize ball_pos and ball_vel for new bal in middle of table
def reset():
    global ball_pos, ball_vel, left_paddle_vel, right_paddle_vel, X, Y  # these are numbers
    ball_vel[0] = 0
    ball_vel[1] = 0
    left_paddle_vel = 0
    right_paddle_vel = 0
    X = 0
    Y = 0
    ball_pos[0] = WIDTH/2
    ball_pos[1] = HEIGHT/2
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_vel # these are vectors stored as lists
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(4, 6)
    elif direction == "LEFT":
        ball_vel[0] = -1 * random.randrange(4, 6)
    ball_vel[1] = random.randrange(4,6)
# define event handlers
def new_game():
    global ball_vel, left_paddle_vel, right_paddle_vel, X, Y, left_score, right_score  # these are ints
    reset()
    left_score = right_score = 0
    spawn_ball(DIRECTION[random.randrange(0,2)])  
def draw(canvas):
    global left_paddle_pos, right_paddle_pos, left_paddle_vel, right_paddle_vel, left_score, right_score, ball_pos, ball_vel, X, Y, Z, pace
    pace = round((ball_vel[0] ** 2 + ball_vel[1] **2) ** 0.5 , 2)
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([0, HEIGHT],[WIDTH, HEIGHT], 1, "White") 
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, "Green", "Yellow")
    # update paddle's vertical position, keep paddle on the screen
    M = max_permissible_range_mod = (HEIGHT/2) - HALF_PAD_HEIGHT
    if X > M:
        X = M
        left_paddle_vel = 0
    elif X < -M:
        X = -M
        left_paddle_vel = 0
    X += left_paddle_vel
    left_paddle_pos = [[0, HEIGHT/2 - HALF_PAD_HEIGHT - X], [PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT - X], [PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT - X], [0, HEIGHT/2 + HALF_PAD_HEIGHT - X]]
    if Y > M:
        Y = M
        right_paddle_vel = 0
    elif Y < -M:
        Y = -M
        right_paddle_vel = 0
    Y += right_paddle_vel
    right_paddle_pos = [[WIDTH - PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT - Y], [WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT - Y], [WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT - Y], [WIDTH - PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT - Y]]
    # draw paddles
    canvas.draw_polygon(left_paddle_pos, 6, 'Blue', 'White')
    canvas.draw_polygon(right_paddle_pos, 6, 'Red', 'White')
    # determine whether paddle and ball collide
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        a = HEIGHT/2 - (HALF_PAD_HEIGHT + BALL_RADIUS) - X
        b = HEIGHT/2 + (HALF_PAD_HEIGHT + BALL_RADIUS) - X
        if ball_pos[1] > a and ball_pos[1] < b:
            if pace < max_pace and pace > -max_pace:
                ball_vel[0] *= -1.1
            elif pace >= max_pace or pace <= -max_pace:
                ball_vel[0] *= -1
        elif ball_pos[1] <= a or ball_pos[1] >= b:
            right_score += 1
            direction = "RIGHT"
            reset()
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        c = HEIGHT/2 - (HALF_PAD_HEIGHT + BALL_RADIUS) - Y
        d = HEIGHT/2 + (HALF_PAD_HEIGHT + BALL_RADIUS) - Y
        if ball_pos[1] > c and ball_pos[1] < d:
            if pace < max_pace and pace > -max_pace:
                ball_vel[0] *= -1.1
            elif pace >= max_pace or pace <= -max_pace:
                ball_vel[0] *= -1
        elif ball_pos[1] <= c or ball_pos[1] >= d:
            left_score += 1
            direction = "LEFT"
            reset()
    # collide and reflect off of bottom side of canvas
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide and reflect off of top side of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # draw scores
    canvas.draw_text(str(left_score) + ' : ' + str(right_score), [WIDTH/2 - 53, HEIGHT+BANNER_HEIGHT/2 + 15], 70, 'GREEN')
    if pace < max_pace:
        if pace < 0.5 * max_pace:
            canvas.draw_text('Pace : '+ str(pace), [WIDTH - 200 , HEIGHT+BANNER_HEIGHT/2 + 15], 40, 'YELLOW')
        else:
            canvas.draw_text('Pace : '+ str(pace), [WIDTH - 200 , HEIGHT+BANNER_HEIGHT/2 + 15], 40, 'ORANGE')
    else:
        canvas.draw_text('MAX PACE!!', [WIDTH - 200 , HEIGHT+BANNER_HEIGHT/2 + 15], 35, 'RED')
def keydown(key):
    global left_paddle_vel, right_paddle_vel
    paddle_acc = 8
    if key == simplegui.KEY_MAP["p"]:
        spawn_ball(direction)
    elif key == simplegui.KEY_MAP["w"]:
        left_paddle_vel += paddle_acc
    elif key == simplegui.KEY_MAP["s"]:
        left_paddle_vel -= paddle_acc
    if key == simplegui.KEY_MAP["up"]:
        right_paddle_vel += paddle_acc
    elif key == simplegui.KEY_MAP["down"]:
        right_paddle_vel -= paddle_acc
def keyup(key):
    #global paddle1_vel, paddle2_vel
    global left_paddle_vel, right_paddle_vel
    left_paddle_vel = right_paddle_vel = 0
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT + BANNER_HEIGHT)
new_game = frame.add_button('Start new game\n', new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
# start frame
frame.start()
