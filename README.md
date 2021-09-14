# Python Application Development (PyDev)


## 1. Pong : 

#### Intro
In this project, we build a version of Pong, one of the first arcade video games (1972). While Pong is not particularly exciting compared to today's video games, it  still kind of a game that one can play and have some fun with. 
Pong is played on a rectangular table. We have a ball that's moving in a straight line and it bounces off the walls in a predictable manner, using basic physics. 

#### Rules
There are two players, and each player controls a paddle using certain keys. We can't move it left and right, we can only move it up and down. On starting the game, the ball moves around on the table. It bounces on the top and bottom walls. When it strikes either of the paddles, it bounces back as well. However, if it misses the paddle & strikes the left gutter, 'Player-2' gets a point. Vice-versa, if it strikes the right gutter, 'Player-1' steals a point. When any player loses a point, the ball stops and positions itself to the centre of the board. The game ends when one of the player manages to score 10 points.

#### Keys
To start the game, we left-click on 'Start new game'.
The keys for 'Player-1' to move the paddle up and down are 'W' and 'S' respectively.
Likewise, 'Player-2' moves the paddles up and down using the 'upper arrow' and 'lower arrow' respectively. 
To resume play after gaining/losing a point, click on 'P'. 

#### Execution
Since the program make use the Python library 'simplegui', that's available only on CodeSkulptor, we cannot directly implement it using  any Python Intrepreter or IDE.\
We recommend using the below URL to directly access the program on CodeSkulptor. For best experience, Chrome or Firefox browser is recommended. 
https://py2.codeskulptor.org/#user48_PJCZaD5pIi_0.py \
Alternatively the code from 'Pong.py' can be copied and pasted on the official CodeSkulptor website, https://py2.codeskulptor.org/ as well. \
To execute the program, we click on 'Run' on Codeskulptor. This opens up a new UI window.<br /><br />


## 2. Space Wars: 

#### Intro
I built a 2D space game RiceRocks that is inspired by the classic arcade game Asteroids (1979). Asteroids is a relatively simple game by today's standards, but was still immensely popular during its time. In the game, the player controls a Spaceship. Large asteroids spawn randomly on the screen with random velocities. The player's goal is to destroy these asteroids before they strike the player's ship.

#### Rules
This is a single-player game where te player controls a Spaceship using certain keys. The Spaceship is controlled via four buttons: two buttons that rotate the spaceship clockwise or counterclockwise (independent of its current velocity), a thrust button that accelerates the ship in its forward direction and a fire button that shoots missiles. It's programmed to keep track of the score and lives remaining.

#### Keys
To start the game, we left-click on 'Start new game'.
The keys to thrust the Spaceship forward is 'W' or the 'up-arrow'.
To rotate the spaceship clockwise we use 'A' or 'left-arrow' key.
Likewise to rotate the spaceship anti-clockwise we use 'D' or 'right-arrow' button.
To shoot missiles, fire the 'Space-bar' key.

#### Execution
Since the program make use the Python library 'simplegui', that's available only on CodeSkulptor, we cannot directly implement it using  any Python Intrepreter or IDE.\
We recommend using the below URL to directly access the program on CodeSkulptor. For best experience, Chrome or Firefox is recommended. 
https://py2.codeskulptor.org/#user48_XFR0nVUQff_0.py \
Alternatively the code from 'Space_Wars.py' can be copied and pasted on the official CodeSkulptor website, https://py2.codeskulptor.org/ as well. \
To execute the program, we click on 'Run' on Codeskulptor. This opens up a new UI window.<br /><br />


## 3. PyHangmanGame : 

This is a simple game of Hangman, wherein one has to arrive at a word by means of guessing the correct set of letters, in a limited number of moves.
On running the code in any of the Python interpreters, we must enter the 'No of players' and 'No of computers', followed by entering one letter at a time and pressing 'Enter'. The code is available as 'PyHangmanGame.py'
