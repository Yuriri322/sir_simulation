"""
Animated visualization of the SIR simulation.

This module creates GIF animations showing how SIR populations evolve over time.
"""

from typing import Tuple
import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sim_sir import simulate_sir
import config


def make_animation(
    t: npt.NDArray,
    S: npt.NDArray,
    I: npt.NDArray,
    R: npt.NDArray,
    save_path: str = "sir.gif",
    title_suffix: str = "",
) -> None:
    """
    Create an animated GIF showing how the SIR populations evolve over time.
    The animation draws the curves progressively to show the dynamics clearly.
    
    Parameters:
        t, S, I, R: Arrays of simulation results
        save_path: Where to save the GIF file
        title_suffix: Additional text for the plot title
    """
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(f"Viral Marketing (SIR) Simulation{title_suffix}", fontsize=14, pad=20)
    ax.set_xlabel("Time", fontsize=12)
    ax.set_ylabel("People", fontsize=12)
    
    # Set axis limits based on data
    ax.set_xlim(0, t[-1])
    ax.set_ylim(0, max(S[0], I.max() if I.max() > 0 else 100, R[-1]) * 1.1)
    ax.grid(True, alpha=0.3)

    # Initialize empty line objects (will be filled progressively during animation)
    lineS, = ax.plot([], [], 'b-', linewidth=2.5, label="Susceptible (S)")
    lineI, = ax.plot([], [], 'r-', linewidth=2.5, label="Spreading (I)")
    lineR, = ax.plot([], [], 'g-', linewidth=2.5, label="Recovered (R)")
    
    # Markers show the current position on each curve
    dotS, = ax.plot([], [], 'bo', markersize=10)
    dotI, = ax.plot([], [], 'ro', markersize=10)
    dotR, = ax.plot([], [], 'go', markersize=10)
    
    ax.legend(loc='upper right', fontsize=11)

    def update(frame):
        """
        Update function called for each animation frame.
        Progressively reveals more of each curve as time advances.
        """
        # Show the curve from start up to the current frame
        # This creates the "drawing" effect as the animation plays
        lineS.set_data(t[:frame+1], S[:frame+1])
        lineI.set_data(t[:frame+1], I[:frame+1])
        lineR.set_data(t[:frame+1], R[:frame+1])
        
        # Update the position of the marker dots
        dotS.set_data([t[frame]], [S[frame]])
        dotI.set_data([t[frame]], [I[frame]])
        dotR.set_data([t[frame]], [R[frame]])
        
        # Return all modified artists for blitting (faster rendering)
        return lineS, lineI, lineR, dotS, dotI, dotR

    # Use every 3rd frame to reduce file size while keeping smooth motion
    frames = list(range(0, len(t), 3))
    
    # Create the animation object
    # interval=50 means 50ms between frames
    # blit=True optimizes rendering by only updating changed parts
    anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

    # Save as GIF using Pillow library
    print(f"Creating animation with {len(frames)} frames...")
    anim.save(save_path, writer="pillow", fps=20)
    plt.close(fig)

def main() -> None:
    """Create and save SIR simulation animation."""
    # ========== CONFIGURATION ==========
    # Initial conditions
    S0, I0, R0 = config.S0, config.I0, config.R0
    
    # Model parameters (modify these to see different behaviors)
    beta = config.BETA
    gamma = config.GAMMA
    
    # Simulation settings
    dt = config.DT
    steps = config.STEPS

    # Calculate R0 (basic reproduction number)
    # R0 > 1: outbreak will occur
    # R0 < 1: outbreak will die out
    r0 = config.get_r0()
    print(f"Running simulation with beta={beta}, gamma={gamma}, R0={r0:.2f}")
    
    # Run the simulation
    t, S, I, R = simulate_sir(S0, I0, R0, beta, gamma, dt, steps)
    
    # Display key results
    print(f"Results: Peak Infected={I.max():.1f}, Final Recovered={R[-1]:.1f}")
    
    # Generate the animated visualization
    make_animation(
        t, S, I, R,
        save_path=config.OUTPUT_FILE,
        title_suffix=f"\nbeta={beta}, gamma={gamma}, R0={r0:.1f}"
    )
    print(f"✓ Saved {config.OUTPUT_FILE}")


if __name__ == "__main__":
    main()
