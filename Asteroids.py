# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
angle_vel = 0
rock_ang_vel = 0
linear_acc = 0
flames = "OFF"
started = False
boom_center = [0, 0]
ang_vel_list = [-0.1, -0.075, -0.05, 0.05, 0.075, 0.1]
vel_list = [-1, -0.5, 0.5, 1]

def play(music):
    """play some music, starts at last paused spot"""
    music.play()

def pause(music):
    """pause the music"""
    music.pause()
    
def rewind(music):
    """rewind the music to the beginning """
    music.rewind()

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([135, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle_vel = angle_vel
        self.angle += self.angle_vel
        self.vel[0] = 0.9*self.vel[0] + linear_acc * math.cos(self.angle)
        self.vel[1] = 0.9*self.vel[1] + linear_acc * math.sin(self.angle)
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if flames is "ON":
            self.image_center = [135, 45]
            play(ship_thrust_sound)
        elif flames is "OFF":
            self.image_center = [45, 45]
            rewind(ship_thrust_sound)

        # Pass through left and right side of canvas
        if self.pos[0] >= WIDTH + 45:
            self.pos[0] = -45
        elif self.pos[0] <= -45:
            self.pos[0] = WIDTH + 45
 
        # Pass through bottom and top side of canvas
        if self.pos[1] >= HEIGHT + 45:
            self.pos[1] = -45
        elif self.pos[1] <= -45:
            self.pos[1] = HEIGHT + 45
  
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        global boom_center
        boom_center[0] = self.image_center[0] + self.image_size[0] * self.age
        boom_center[1] = self.image_center[1]
        if self.animated == True:
            canvas.draw_image(self.image, [boom_center[0],boom_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.age += 1
        if self.age >= (self.lifespan):
            return True
        else:
            self.angle += self.angle_vel
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]     
            # Pass through left and right side of canvas
            if self.pos[0] >= WIDTH + 45:
                self.pos[0] = -45
            elif self.pos[0] <= -45:
                self.pos[0] = WIDTH + 45
            # Pass through bottom and top side of canvas
            if self.pos[1] >= HEIGHT + 45:
                self.pos[1] = -45
            elif self.pos[1] <= -45:
                self.pos[1] = HEIGHT + 45
            return False
            
    def collide(self, other_object):
        p = other_object.pos
        q = self.pos
        r1 = other_object.radius
        r2 = self.radius
        d = dist(p,q)
        if d <= (r1 + r2):
            return True
        return False
            
    
def shoot():
    global missile_group
    missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
    missile.pos[0] = my_ship.pos[0] + 45*math.cos(my_ship.angle)
    missile.pos[1] = my_ship.pos[1] + 45*math.sin(my_ship.angle)
    missile.vel[0] = 1.5 * my_ship.vel[0] + 3*math.cos(my_ship.angle)
    missile.vel[1] = 1.5 * my_ship.vel[1] + 3*math.sin(my_ship.angle)
    missile_group.add(missile)   
            
        
        
def group_collide(group, other_object):
    global lives, started, score, rock_group, timer
    asteroids = set(group)
    for rock in asteroids:
        if rock.collide(other_object):
            explosion = Sprite(rock.pos, [0, 0], 0, 0, explosion_image, explosion_info)
            explosion_group.add(explosion)
            explosion_sound.rewind()
            explosion_sound.play()
            group.remove(rock)
            lives -= 1

def group_group_collide(rock_group, missile_group):
    global score
    rocks = set(rock_group)
    missiles = set(missile_group)
    for rock in rocks:
        for missile in missiles:
            if missile.collide(rock):
                explosion = Sprite(rock.pos, [0, 0], 0, 0, explosion_image, explosion_info)
                explosion_group.add(explosion)
                explosion_sound.play()
                rock_group.remove(rock)
                missile_group.remove(missile)
                score += 1

        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, timer
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        score = 0
        lives = 3
        started = True
        timer.start()
        rewind(soundtrack)
        play(soundtrack)


def draw(canvas):
    global time, started, rock_group, missile_group, explosion_group
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw UI
    group_collide(rock_group, my_ship)
    group_group_collide(rock_group, missile_group)
    canvas.draw_text('Score : ' + str(score), [53, 50], 30, 'WHITE')
    canvas.draw_text('Lives remaining : ' + str(lives) , [WIDTH - 300, 50], 30, 'WHITE')

    # draw ship and sprites
    my_ship.draw(canvas)
    #a_rock.draw(canvas)
    #a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    #a_rock.update()
    #a_missile.update()
    
    # process sprite group
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)

    # draw splash screen if not started
    if lives == 0:
        started = False
        timer.stop()
        soundtrack.pause()
        soundtrack.rewind()
        ship_thrust_sound.pause()
        ship_thrust_sound.rewind()
        explosion_group = set([])        
        rock_group = set([])
        missile_group = set([])
        canvas.draw_text("Game over!!", (580, 580), 40, 'red') 

    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if len(rock_group) < 12:
        rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info) 
        x = [random.randrange(90, 180), random.randrange(WIDTH-180, WIDTH-90)]
        y = [random.randrange(90, 180), random.randrange(HEIGHT-180, HEIGHT-90)]
        rock.pos[0] = x[random.randrange(0, 2)]
        rock.pos[1] = y[random.randrange(0, 2)]
        rock.vel[0] = vel_list[random.randrange(0,4)]
        rock.vel[1] = vel_list[random.randrange(2,4)]
        rock.angle_vel = ang_vel_list[random.randrange(len(ang_vel_list))]
        rock_group.add(rock)
    
def process_sprite_group(sprite_group, canvas):
    sprite_group_copy = set(sprite_group)
    for sprite in sprite_group_copy:
        sprite.draw(canvas)
        if sprite.update():
            sprite_group.remove(sprite)

    
# keydown and keyup handlers

def keydown(key):
    global angle_vel, linear_acc, flames
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["a"]:
        angle_vel = -0.1
    elif key == simplegui.KEY_MAP["right"] or key == simplegui.KEY_MAP["d"]:
        angle_vel = 0.1
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["w"]:
        linear_acc = 1
        flames = "ON"
    elif key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["s"]:
        linear_acc = -0.5
    elif key == simplegui.KEY_MAP["space"]:
        shoot()
        rewind(missile_sound)
        play(missile_sound)

        
def keyup(key):
    global angle_vel, linear_acc, flames
    if key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["a"] or key == simplegui.KEY_MAP["right"] or key == simplegui.KEY_MAP["d"]:
        angle_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["s"]:
        linear_acc = 0
        flames = "OFF"
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set([])
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
missile_group = set([])
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)


timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
frame.start()

