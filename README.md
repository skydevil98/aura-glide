# Aura Glide

Aura Glide is a modern, fast-paced, side-scrolling arcade game built with Python and Pygame. Navigate your way through endless obstacles, achieve new high scores, and enjoy slick, dynamically generated visual effects and synthesized audio!

## Features
- **Smooth Physics**: Flappy-style gravity and jump mechanics.
- **Dynamic Particle System**: Beautiful ambient particles on the menu, a sleek trail following the player, and satisfying explosion effects on impact.
- **Procedurally Generated Audio**: The game synthesizes its own sound effects (flap, score, crash) and background music procedurally on the first run using Python's `math` and `wave` modules. No external audio files to download!
- **Sleek, Modern UI**: Clean typography and transparent panels. Includes full state management (Main Menu, Playing, Paused, and Game Over).
- **Async-Ready Loop**: The game uses `asyncio` for its main loop, making it easier to integrate or compile for web targets (like `pygbag`).

## Prerequisites
- Python 3.7+
- [uv](https://github.com/astral-sh/uv) (optional, but recommended for fast dependency management)

## Installation

1. **Clone the repository** (if applicable) or navigate to the game directory:
   ```bash
   cd aura-glide
   ```

2. **Install requirements**:
   We recommend using `uv` to install the dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```
   Or using standard `pip`:
   ```bash
   pip install -r requirements.txt
   ```
   *(The only external dependency is `pygame`.)*

## How to Play

Start the game using:
```bash
python main.py
```

### Controls
- **SPACE**: Flap / Jump. (Also starts the game from the Main Menu and restarts from the Game Over screen).
- **ESC**: Pause / Resume the game.
- **Mouse Click (Left)**: Navigate menus or flap during gameplay.

## Project Structure
- `main.py`: Contains the core game loop, event handling, collision detection, and state machine.
- `settings.py`: Game constants, screen dimensions, velocities, and color palettes.
- `entities.py`: Classes defining the `Player` and `Obstacle` behaviors.
- `particles.py`: Defines the `Particle` and `ParticleSystem` for rendering visual effects.
- `ui.py`: Reusable UI components like `Button`, `TextRenderer`, and drawing functions.
- `assets/sounds/`: Automatically generated directory that stores the synthesized `.wav` audio files.
