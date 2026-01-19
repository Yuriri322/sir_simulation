import numpy as np

# Calculate derivatives for the SIR model
import numpy as np



def sir_derivatives(S, I, R, beta, gamma):
    """
    Calculate the rate of change for each compartment in the SIR model.
    
    The SIR model divides the population into three groups:
    - S: Susceptible (can catch the trend)
    - I: Infected (actively spreading the trend)
    - R: Recovered (no longer spreading)
    
    Parameters:
        S, I, R: Current population in each compartment
        beta: Transmission rate (how easily the trend spreads)
        gamma: Recovery rate (how quickly people stop spreading)
    
    Returns:
        (dS/dt, dI/dt, dR/dt): Rate of change for each compartment
    """
    # Total population (remains constant throughout simulation)
    N = S + I + R
    
    # Rate of new infections: proportional to S*I interactions
    # Divided by N to get the contact probability
    dS = -beta * S * I / N
    
    # Infected change: gain new infections, lose to recovery
    dI = beta * S * I / N - gamma * I
    
    # Recovery rate: proportional to current infected
    dR = gamma * I
    
    return dS, dI, dR

def simulate_sir(S0, I0, R0, beta, gamma, dt, steps):
    """
    Simulate the SIR model over time using Euler's numerical method.
    
    Euler's method approximates the solution to differential equations by:
    new_value = old_value + (rate_of_change * time_step)
    
    Parameters:
        S0, I0, R0: Initial population in each compartment
        beta: Transmission rate (0 to 1+)
        gamma: Recovery rate (0 to 1)
        dt: Time step size (smaller = more accurate)
        steps: Number of simulation steps
    
    Returns:
        t: Time array
        S, I, R: Population arrays for each compartment over time
    """
    # Initialize arrays to store results at each time step
    t = np.zeros(steps + 1)  # Time points
    S = np.zeros(steps + 1)  # Susceptible over time
    I = np.zeros(steps + 1)  # Infected over time
    R = np.zeros(steps + 1)  # Recovered over time

    # Set initial conditions at time t=0
    S[0], I[0], R[0] = S0, I0, R0

    # Simulate each time step using Euler's method
    for k in range(steps):
        # Calculate rates of change at current state
        dS, dI, dR = sir_derivatives(S[k], I[k], R[k], beta, gamma)

        # Euler's method: new = old + rate * dt
        S[k + 1] = S[k] + dt * dS
        I[k + 1] = I[k] + dt * dI
        R[k + 1] = R[k] + dt * dR
        t[k + 1] = t[k] + dt

        # Prevent negative populations (can occur due to numerical errors)
        S[k + 1] = max(S[k + 1], 0.0)
        I[k + 1] = max(I[k + 1], 0.0)
        R[k + 1] = max(R[k + 1], 0.0)

    return t, S, I, R

if __name__ == "__main__":
    # ========== SIMULATION PARAMETERS ==========
    # Initial population distribution
    S0, I0, R0 = 990, 10, 0  # Start with 990 susceptible, 10 infected, 0 recovered
    
    # Model parameters
    beta = 0.08   # Transmission rate
    gamma = 0.10  # Recovery rate
    # R0 = beta/gamma = 0.8 (trend will die out since R0 < 1)
    
    # Numerical simulation settings
    dt = 0.1      # Time step (smaller = more accurate but slower)
    steps = 600   # Number of steps (total time = 600 * 0.1 = 60 time units)

    # Run the simulation
    t, S, I, R = simulate_sir(S0, I0, R0, beta, gamma, dt, steps)

    # Verify conservation of population (important validation check)
    # The total N = S + I + R should remain constant throughout
    total = S + I + R
    print("Total population (min/max):", total.min(), total.max())
    print("Expected:", S0 + I0 + R0)
