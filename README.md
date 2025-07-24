# Crossy Game

This repository contains a simple Crossy Road style game implemented with [pygame](https://www.pygame.org/).
It also includes a SpriteKit version for iOS written in Swift.

## Requirements

- Python 3
- pygame

Install dependencies (if not already installed):

```bash
pip install pygame
```

## Running the Game

Run the game using:

```bash
python3 crossy_game.py
```

Use the arrow keys to move the player and cross the lanes without hitting cars. Each time you reach the top of the screen, your score increases and the level resets.

## iOS Version

The `crossy_game.swift` file contains a SpriteKit implementation suitable for an iOS project.
Create a new SpriteKit game in Xcode and replace the default `GameScene.swift`
with the contents of `crossy_game.swift` to play the game on an iOS device or
simulator.
