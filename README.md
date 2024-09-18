# Zombie Evaders

**Zombie Evaders** is a 2D action-shooter game built using Python and the Pygame library. The player controls a soldier who must evade and shoot zombies while trying to survive. The goal is to defeat as many zombies as possible before they reach the player.

## Features

- **Player Movement**: The player can move up and down along the screen to dodge incoming enemies.
- **Shooting Mechanism**: The player can fire bullets to destroy zombies.
- **Enemies**: Multiple zombies come toward the player. The player must shoot them before they reach the left side of the screen.
- **Collision Detection**: Bullets can collide with enemies to destroy them, and the player gains points for each successful hit.
- **Game Over**: If a zombie reaches the player’s side, the game is over.

## How to Play

- Use the **Up Arrow** key to move the soldier up.
- Use the **Down Arrow** key to move the soldier down.
- Press the **Spacebar** to fire bullets and shoot the zombies.
- Your score increases by 1 for every zombie you destroy.
- If any zombie reaches the player's side, the game ends.

## Game Controls

- **Up Arrow**: Move the soldier up.
- **Down Arrow**: Move the soldier down.
- **Spacebar**: Shoot bullets.

## Installation and Setup

1. Install Python from the official [Python website](https://www.python.org/).
2. Install Pygame by running the following command in your terminal or command prompt:
   ```bash
   pip install pygame
   ```
3. Clone or download this repository to your local machine.

4. Ensure you have the following asset files in the same directory as the game:
   - `background.png`: The background image for the game.
   - `soldier.png`: Icon for the game and the image for the player character.
   - `enemy.png`: Image for the zombie enemies.
   - `bullet.png`: Image for the bullets fired by the player.
   - `backgroundsound.mp3`: Background music for the game.

5. Run the game:
   ```bash
   python zombie_evaders.py
   ```

## Project Structure

```plaintext
zombie_evaders/
│
├── images/
│   ├── background.png         # Background image for the game
│   ├── soldier.png            # Player character (soldier) image
│   ├── enemy.png              # Zombie enemy image
│   ├── bullet.png             # Bullet image
│   ├── backgroundsound.mp3    # Background music
│   ├── Test image1.PNG        # Test image 1
│   └── Test image2.PNG        # Test image 2
└── zombie_evaders.py          # Main game script

```

## Dependencies

- **Python 3.8+**
- **Pygame**: Install Pygame using `pip install pygame`.

## Future Improvements

- Add different levels with increasing difficulty.
- Introduce more types of enemies with different speeds and behaviors.
- Add power-ups or health packs for the player.
- Implement a high-score system to track the best scores across game sessions.

## License

This project is free to use and distribute. Modify it as you see fit!
