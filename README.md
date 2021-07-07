# Space Adventure (space invaders)

Space Adventure is a game based on space invaders and created with Pygame library. 

![print](cover.png)

## Gameplay  

To play the game, use :
 
- `LEFT ARROW` to move left,
- `RIGHT ARROW` to move right,
- `SPACE` to shoot enemies  
  

## Getting Started

![play](https://github.com/alicevillar/space-invaders/blob/main/ezgif.gif)


### Install

1. Install Python and pygame ==> `pip install pygame==2.0.1`

2. Clone and copy this repository

```
$ git clone https://github.com/alicevillar/space-invaders
```

3. `python main.py`
  

### Resources:

I started this project when I saw the [demonstration](https://www.youtube.com/watch?v=FfWpgLFMI7w&t=6893s) from [attreyabhatt](https://github.com/attreyabhatt). I studied his [project](https://github.com/attreyabhatt/Space-Invaders-Pygame)) and created my own version. :smiley: ! 

The architecture is similar, but I implemented several new features, which changed the code a lot:

* Layout - New Images, Sounds and Background Music 
* Sizes - ider window and different sizes for the player and enemies
* Enemies - I included a another list of enemies. In my game there are two groups: comets and ets (foreign spaceships) 
* flip() - Instead of creating a second PNG image file for the comet, I used pygame. transform. flip() function. This function has three parameters: the Surface object with the image to flip, a Boolean value to do a horizontal flip, and a Boolean value to do a vertical flip. Since the comet has a tail, this function allows it to flip to the right and to the left and it hits the border. 
* You Win - When the player shoots 30 enemies, he or she wins. To celebrate the vitory, I included a vitory background to replace the main backkground. 
* bitwise XOR (^) - Since in my game there are two lists of enemies (comets and ets), it was necessary to create two sets of collision. Thus, a Bitwise XOR (exclusive OR) was necessary when checking the collision. Without it, the collision wasn't beeing properlly recognized. 
