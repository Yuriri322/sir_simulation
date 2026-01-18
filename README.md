# SIR Model Simulation

Python implementation of the SIR (Susceptible-Infected-Recovered) model that simulates how trends or diseases spread through a population.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Generate an animated GIF:
```bash
python src/sim_sir_animation.py
```

Run basic simulation:
```bash
python src/sim_sir.py
```

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

Edit these in `src/sim_sir_animation.py`:

- **beta** (β): Transmission rate (how fast it spreads)
- **gamma** (γ): Recovery rate (how fast people stop spreading)
- **R₀ = β/γ**: Basic reproduction number
  - R₀ > 1: outbreak spreads
  - R₀ < 1: outbreak dies out

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
