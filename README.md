# Virtual Pet Clicker

A simple virtual pet clicker game built with Pygame where you can interact with a cat by clicking on its head, body, tail, and paws. The cat responds with sounds and animations.

## Features

- Click on different parts of the cat to trigger sounds and animations.
- The cat's head, tail, and paws animate with random movements.
- Sounds include purring, meowing, and chirping.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ash250604/virtual-pet-clicker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd virtual-pet-clicker
    ```
3. Install the required dependencies:
    ```bash
    pip install pygame
    ```
4. Ensure you have the sound files (`purr.wav`, `meow.wav`, `chirp.wav`) in the same directory as the script.

## How to Play

1. Run the game:
    ```bash
    python main.py
    ```
2. Interact with the cat by clicking on its head, body, tail, and paws.
3. Enjoy the animations and sounds as the cat responds to your clicks.

## Code Overview

- **Colors Used**: Defines the colors used in the game.
- **Sound Loading**: Loads the sounds for purring, meowing, and chirping.
- **Draw Cat Function**: Draws the cat on the screen and handles the animation and clicking effects.
- **Main Game Loop**: Manages the game state, handles events, and updates the screen.
