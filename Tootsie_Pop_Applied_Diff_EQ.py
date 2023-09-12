import numpy as np
from scipy.integrate import solve_ivp
import argparse

# Constants
tootsie_pop_radius = 0.5  # Radius of the Tootsie Pop (in inches)
dissolution_rate = 0.02  # Rate of dissolution per lick (in inches per lick)

# Define the differential equation
def tootsie_pop_licks(t, y):
    remaining_radius = y[0]
    d_radius_dt = -dissolution_rate
    return [d_radius_dt]

# Command-line input
parser = argparse.ArgumentParser(description="Calculate remaining licks to the center of a Tootsie Pop.")
parser.add_argument("initial_licks", type=int, help="Initial number of licks taken.")
args = parser.parse_args()

# Calculate the initial radius based on the initial number of licks
initial_radius = tootsie_pop_radius - (args.initial_licks * dissolution_rate)

# Set up the time span for integration
t_span = (0, np.inf)

# Set up the initial conditions
initial_conditions = [initial_radius]

# Solve the differential equation
solution = solve_ivp(tootsie_pop_licks, t_span, initial_conditions, dense_output=True)

# Function to calculate the remaining licks
def remaining_licks(t):
    remaining_radius = solution.sol(t)[0]
    return int((tootsie_pop_radius - remaining_radius) / dissolution_rate)

# Calculate and print the remaining licks
remaining_licks_result = remaining_licks(0)
print(f"Remaining licks to reach the center: {remaining_licks_result}")
