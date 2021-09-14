# Python Application Development (PyDev)


## 1. Pong : 

#### Intro
In this project, we build a version of Pong, one of the first arcade video games (1972). While Pong is not particularly exciting compared to today's video games, it  still kind of a game that one can play and have some fun with. 
Pong is played on a rectangular table. We have a ball that's moving in a straight line and it bounces off the walls in a predictable manner, using basic physics. 

#### Rules
There are two players, and each player controls a paddle using certain keys. We can't move it left and right, we can only move it up and down. On starting the game, the ball moves around on the table. It bounces on the top and bottom walls. When it strikes either of the paddles, it bounces back as well. However, if it misses the paddle & strikes the left gutter, 'Player-2' gets a point. Vice-versa, if it strikes the right gutter, 'Player-1' steals a point. When any player loses a point, the ball stops and positions itself to the centre of the board. The game ends when one of the player manages to score 10 points.

#### Keys
- To start the game, we left-click on 'Start new game'.
- The keys for 'Player-1' to move the paddle up and down are 'W' and 'S' keys respectively.
- Likewise, 'Player-2' moves the paddles up and down using the 'up-arrow' and 'down-arrow' keys respectively. 
- To resume play after gaining/losing a point  use the key 'P'. 

#### Execution
Since the program make use the Python library 'simplegui', that's available only on CodeSkulptor, we cannot directly implement it using  any Python Intrepreter or IDE.\
We recommend using the below URL to directly access the program on CodeSkulptor. For best experience, Chrome or Firefox browser is recommended. 
https://py2.codeskulptor.org/#user48_PJCZaD5pIi_0.py \
Alternatively the code from 'Pong.py' can be copied and pasted on the official CodeSkulptor website, https://py2.codeskulptor.org/ as well. \
To execute the program, we click on 'Run' on Codeskulptor. This opens up a new UI window.<br /><br />


## 2. Space Wars: 

#### Intro
The 2D space game Space Wars is inspired by the classic arcade game Asteroids (1979). It's simple game by today's standards, but was still immensely popular during its time. In the game, the player controls a Spaceship. Large asteroids spawn randomly on the screen with random velocities. The player's goal is to destroy these asteroids before they strike the player's ship.

#### Rules
This is a single-player game where te player controls a Spaceship using certain keys. The Spaceship is controlled via four buttons: two buttons that rotate the spaceship clockwise or counterclockwise (independent of its current velocity), a thrust button that accelerates the ship in its forward direction and a fire button that shoots missiles. It's programmed to keep track of the score and lives remaining.

#### Keys
- To start the game, we left-click on 'Start new game'.
- To thrust the Spaceship forward we use 'W' or the 'up-arrow' key.
- To rotate the spaceship clockwise we use 'A' or the 'left-arrow' key.
- Likewise to rotate the spaceship anti-clockwise we use 'D' or the 'right-arrow' key.
- To shoot missiles, fire the 'Space-bar' key.

#### Execution
Since the program make use the Python library 'simplegui', that's available only on CodeSkulptor, we cannot directly implement it using  any Python Intrepreter or IDE.\
We recommend using the below URL to directly access the program on CodeSkulptor. For best experience, Chrome or Firefox is recommended. 
https://py2.codeskulptor.org/#user48_XFR0nVUQff_0.py \
Alternatively the code from 'Space_Wars.py' can be copied and pasted on the official CodeSkulptor website, https://py2.codeskulptor.org/ as well. \
To execute the program, we click on 'Run' on Codeskulptor. This opens up a new UI window.<br /><br />


## 3. Blackjack: 

#### Description
Blackjack is a simple, popular card game that is played in many casinos. Cards in Blackjack have the following values: an ace may be valued as either 1 or 11 (player's choice), face cards (kings, queens and jacks) are valued at 10 and the value of the remaining cards corresponds to their number. During a round of Blackjack, the players plays against a dealer with the goal of building a hand (a collection of cards) whose cards have a total value that is higher than the value of the dealer's hand, but not over 21.  (A round of Blackjack is also sometimes referred to as a hand.)

#### Rules
- The player and the dealer are each dealt two cards initially with one of the dealer's cards being dealt faced down (his hole card). 
- The player may then ask for the dealer to repeatedly "hit" his hand by dealing him another card.
-  If, at any point, the value of the player's hand exceeds 21, the player is "busted" and loses immediately. 
-  At any point prior to busting, the player may "stand" and the dealer will then hit his hand until the value of his hand is 17 or more. (For the dealer, aces count as 11 unless it causes the dealer's hand to bust).
-   If the dealer busts, the player wins. 
-   Otherwise, the player and dealer then compare the values of their hands and the hand with the higher value wins. 
-   The dealer wins ties.

#### Keys
- To start the game, we left-click on 'Start new game'. This opens a new UI tab.
- We left-click on 'Deal','Hit' or 'Stand' in the game's UI to perform the respective actions.

#### Execution
Since the program make use the Python library 'simplegui', that's available only on CodeSkulptor, we cannot directly implement it using  any Python Intrepreter or IDE.\
We recommend using the below URL to directly access the program on CodeSkulptor. For best experience, Chrome or Firefox is recommended. 
https://py2.codeskulptor.org/#user48_XFR0nVUQff_0.py \
Alternatively the code from 'Space_Wars.py' can be copied and pasted on the official CodeSkulptor website, https://py2.codeskulptor.org/ as well. \
To execute the program, we click on 'Run' on Codeskulptor. This opens up a new UI window.<br /><br />


## 4. PyHangmanGame : 

This is a simple game of Hangman, wherein one has to arrive at a word by means of guessing the correct set of letters, in a limited number of moves.
On running the code in any of the Python interpreters, we must enter the 'No of players' and 'No of computers', followed by entering one letter at a time and pressing 'Enter'. The code is available as 'PyHangmanGame.py'
