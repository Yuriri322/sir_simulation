"""
Configuration settings for SIR simulation.
Modify these parameters to experiment with different scenarios.
"""

# Initial population distribution
S0: int = 990  # Susceptible individuals
I0: int = 10   # Infected individuals
R0: int = 0    # Recovered individuals

# Model parameters
BETA: float = 0.30    # Transmission rate (β) - how easily infection spreads
GAMMA: float = 0.10   # Recovery rate (γ) - how quickly people recover
# R₀ (basic reproduction number) = BETA / GAMMA
# R₀ > 1: outbreak will spread
# R₀ < 1: outbreak will die out

# Numerical simulation settings
DT: float = 0.1       # Time step (smaller = more accurate but slower)
STEPS: int = 600      # Number of simulation steps

# Animation settings
ANIMATION_INTERVAL: int = 50    # Milliseconds between frames
ANIMATION_FPS: int = 20         # Frames per second
ANIMATION_FRAME_SKIP: int = 3   # Show every nth frame
OUTPUT_FILE: str = "sir.gif"    # Output filename
FIGURE_SIZE: tuple = (10, 6)    # Figure size in inches
FIGURE_DPI: int = 100           # Figure DPI


def get_r0() -> float:
    """Calculate the basic reproduction number (R₀)."""
    return BETA / GAMMA


def get_total_population() -> int:
    """Get total population."""
    return S0 + I0 + R0
