# Small Games
- Some games to test and play.
- "How to play" is included in README.md in their respective directories
- main.py is the entrypoint for all games
- Remember to cd into the project directories before running main.py ~

# Package manager
- uv

# Format and linter
- ruff 


# Programming concepts learnt from projects in this repo
- Conway's Game of Life
    - Key Reading 
    - Time Progression

- BallCircle
    - Physics Calculations (Gravity, Collision, etc.)
    - Delta time (makes movement, physics, and animations frame-rate independent)
    - Initial game configs
    - Current program state

- Spaceship
    - Mixins (Plugins that include certain functionalities)
    - Finding assets
    - Reset / Reuse objects instead of destroying and recreating them
    - Drawing text and importing images
    - @property and @abstractmethods
    - Extending classes using dunder methods for arithmethic operations (\_\_add\_\_), iterations (\_\_iter\_\_) and if object is within (\_\_contains\_\_)
    - ruff for format checking and fix
    - ruff extensions within pyproject.toml
    - Wrapping around indexes and coordinates using modulo (%)