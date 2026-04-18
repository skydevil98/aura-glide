# Aura Glide

Aura Glide is a modern, fast-paced, side-scrolling arcade game built with Python and Pygame. Navigate your way through endless obstacles, achieve new high scores, and enjoy slick, dynamically generated visual effects and synthesized audio!

## Features
- **Smooth Physics**: Flappy-style gravity and jump mechanics.
- **Dynamic Particle System**: Beautiful ambient particles on the menu, a sleek trail following the player, and satisfying explosion effects on impact.
- **Procedurally Generated Audio**: The game synthesizes its own sound effects (flap, score, crash) and background music procedurally on the first run using Python's `math` and `wave` modules. No external audio files to download!
- **Sleek, Modern UI**: Clean typography and transparent panels. Includes full state management (Main Menu, Playing, Paused, and Game Over).
- **Async-Ready Loop**: The game uses `asyncio` for its main loop, making it compatible with web targets via `pygbag`.
- **Web Export Ready**: Ships with `pygbag` for easy browser-based builds.

## Prerequisites
- Python 3.7+

## Installation

1. **Clone the repository** or navigate to the game directory:
   ```bash
   cd aura-glide
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate       # macOS / Linux
   # venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r src/requirements.txt
   ```
   This installs:
   - `pygame==2.6.1` — game engine
   - `pygbag==0.9.3` — web/browser export support

## How to Play

Start the game using:
```bash
python main.py
```

### Controls
- **SPACE**: Flap / Jump. (Also starts the game from the Main Menu and restarts from the Game Over screen.)
- **ESC**: Pause / Resume the game.
- **Mouse Click (Left)**: Navigate menus or flap during gameplay.

## Project Structure

```
aura-glide/
├── main.py               # Core game loop, event handling, collision detection, state machine
├── assets/
│   └── sounds/           # Auto-generated synthesized .wav audio files (created on first run)
├── build/                # Output directory for web/pygbag builds
├── src/
│   ├── requirements.txt  # Project dependencies (pygame, pygbag)
│   ├── entities.py       # Player and Obstacle class definitions
│   ├── particles.py      # Particle and ParticleSystem for visual effects
│   └── ...               # Additional modules (settings, ui, etc.)
└── venv/                 # Local virtual environment (not committed to version control)
```

## Web Export (pygbag)

To build and run the game in a browser:
```bash
python -m pygbag main.py
```
Then open `http://localhost:8000` in your browser.
