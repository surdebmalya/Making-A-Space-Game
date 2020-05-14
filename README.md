# Making-A-Space-Game
Let's make a space game.
In this space game we will have a space ship and some enemies will moving in the screen from left to right and when they comes to the rightmost area, they will quickly come downwards for a certain distance and then start moving from right to left.
Opposite rule goes for the movement from right to left.
Our space ship can only moves right and left by pressing the arrow keys or D or A from keyboard.
We can also shoot by pressing Spacebar.
If any enemy can reach a certain red line then the game will be over.
## See the game in action:
[![Watch the video](https://img.youtube.com/vi/sH9s29FHY1Y/0.jpg)](https://youtu.be/sH9s29FHY1Y)
## Game Mechanisms & Building Idea:
- The game is a basic implementation of one of the best modules that is used for python game development, i.e. pygame module. 
- In pygame every objects is been defined first and then it has been placed on the suitable position of the screen. 
- In this game just 5 keys will be active, i.e. by pressing 'a' or '<-' key you will move towards left, ny pressing 'd' or '->' key you can move towards right and by pressing space bar, you can shoot a bullet. These functionalities can be easily implemented by pygame modules.
- Next step, you have to make conditions such that, your character should not go beyond your game screen, for that you have to implement if-else conditions.
- Then you have to place the enemies, i.e. where the enemies should start moving and how long they will move as well as what to do when they hit the boundaries of the game screen.
## Where the enemies should start moving:
- Well, it is dependent upon your creativity, how you want to build your game. If you want to define a suitable position from where the new enemies will start moving after one's death, then you can put the location of that position, or you can use the **random** module, by which you can generate new enemies any where in the game window.
## How long they will move:
- It's the simple answer, they will move until they will hit by a bullet. So, here comes the main thing, **Collision**. So you have to define the collision function seperately, by which in every fps the game loop will check for the return value of the collision function. If it is True, i.e. collision happens, so you have to destroy the current enemy by which the collision has just happended and also you have to generate a new enemy.
## What to do when the enemy hits the boundaries of the game screen:
- Again, it's dependent upon you. Here, I have structured the game as a manner such that, when a enemy will hit the game boundaries, they will come down for a certain distance and it will start moving to the opposite direction of previous, until it is hhit by a bullet or if it can reaches to the red line then the game will end.
## How to download the game:
- Visit https://dsasanengineer.blogspot.com/2020/04/download-simple-space-game-made-by-me.html, and download the game!!!

For more details please visit:
https://dsasanengineer.blogspot.com/2020/01/making-space-ship-game-by-pygame.html
