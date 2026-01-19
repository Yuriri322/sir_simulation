# SIR Model Simulation

![Python Tests and Linting](https://github.com/Yuriri322/sir_simulation/workflows/Python%20Tests%20and%20Linting/badge.svg)

Python implementation of the SIR (Susceptible-Infected-Recovered) model that simulates how trends or diseases spread through a population.

## Quick Start

### Installation

```bash
git clone https://github.com/Yuriri322/sir_simulation.git
cd sir_simulation
pip install -r requirements.txt
```

### Usage

Generate an animated GIF:
```bash
python src/sim_sir_animation.py
```

Run basic simulation:
```bash
python src/sim_sir.py
```

### Configuration

Edit `config.py` to customize simulation parameters:

```python
S0 = 990        # Initial susceptible population
I0 = 10         # Initial infected population
BETA = 0.30     # Transmission rate
GAMMA = 0.10    # Recovery rate
```

## Features

✅ Configurable SIR model parameters  
✅ Animated GIF generation  
✅ Type hints for better code quality  
✅ Detailed documentation and comments  
✅ Automatic validation of population conservation  
✅ GitHub Actions CI/CD pipeline  

## How It Works

The population is divided into three groups:
- **S (Susceptible)**: Can catch the trend
- **I (Infected)**: Actively spreading
- **R (Recovered)**: No longer spreading

The model uses these equations:

$$\frac{dS}{dt} = -\beta \frac{SI}{N}$$

$$\frac{dI}{dt} = \beta \frac{SI}{N} - \gamma I$$

$$\frac{dR}{dt} = \gamma I$$

## Parameters

All parameters are managed in `config.py`:

- **S0, I0, R0**: Initial population distribution
- **BETA (β)**: Transmission rate (how fast it spreads)
- **GAMMA (γ)**: Recovery rate (how fast people stop spreading)
- **R₀ = β/γ**: Basic reproduction number
  - R₀ > 1: outbreak spreads
  - R₀ < 1: outbreak dies out
- **DT**: Time step for simulation
- **STEPS**: Number of simulation steps
- **Animation parameters**: Frame rate, output format, etc.

## Examples

**Fast spread (R₀ = 3.0):**
```python
beta, gamma = 0.30, 0.10
```

**Slow spread (R₀ = 1.5):**
```python
beta, gamma = 0.15, 0.10
```

**Dies out (R₀ = 0.8):**
```python
beta, gamma = 0.08, 0.10
```
