import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sim_sir import simulate_sir  

def make_animation(t, S, I, R, save_path="sir.gif", title_suffix=""):
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

if __name__ == "__main__":
    # ========== CONFIGURATION ==========
    # Initial conditions
    S0, I0, R0 = 990, 10, 0  # 990 susceptible, 10 initially spreading
    
    # Model parameters (modify these to see different behaviors)
    beta = 0.30   # Transmission rate (higher = spreads faster)
    gamma = 0.10  # Recovery rate (higher = shorter infection period)
    
    # Simulation settings
    dt = 0.1      # Time step
    steps = 600   # Number of steps (total time = 60 units)

    # Calculate R0 (basic reproduction number)
    # R0 > 1: outbreak will occur
    # R0 < 1: outbreak will die out
    print(f"Running simulation with β={beta}, γ={gamma}, R₀={beta/gamma:.2f}")
    
    # Run the simulation
    t, S, I, R = simulate_sir(S0, I0, R0, beta, gamma, dt, steps)
    
    # Display key results
    print(f"Results: Peak Infected={I.max():.1f}, Final Recovered={R[-1]:.1f}")
    
    # Generate the animated visualization
    make_animation(t, S, I, R, save_path="sir.gif", 
                   title_suffix=f"\nβ={beta}, γ={gamma}, R₀={beta/gamma:.1f}")
    print("✓ Saved sir.gif")
