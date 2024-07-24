import numpy as np
import matplotlib.pyplot as plt

# Number of simulations
num_simulations = 1000000

# Initial probabilities based on provided information
initial_probs = [0.1, 0.2, 0.25, 0.3, 0.125, 0.025, 0.0]  # Including August with 0 initial probability
months = ["Feb 2024", "Mar 2024", "Apr 2024", "May 2024", "Jun 2024", "Jul 2024", "Aug 2024"]

# Adjusted potential delays
potential_delays = [0, 1, 2, 3, 4]  # No delay, 1 month delay, etc.
delay_probabilities = [0.75, 0.15, 0.075, 0.02, 0.005]  # Realistic probabilities for delays

# Simulate readout timings
readout_timings = []

for _ in range(num_simulations):
    initial_month = np.random.choice(months[:-1], p=initial_probs[:-1])  # Exclude August in initial choice
    delay = np.random.choice(potential_delays, p=delay_probabilities)
    readout_month_index = min(months.index(initial_month) + delay, len(months) - 1)
    readout_timings.append(months[readout_month_index])

# Aggregate results
timing_counts = {month: readout_timings.count(month) for month in months}
timing_probabilities = {month: count / num_simulations for month, count in timing_counts.items()}

for month, count in timing_probabilities.items():
    print(month, count)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.bar(timing_probabilities.keys(), timing_probabilities.values(), color='skyblue')
plt.xlabel('Month')
plt.ylabel('Probability')
plt.title('Probability Distribution of BiotechA Phase III Data Readout Timing')
plt.ylim(0, 0.5)
plt.grid(True)
plt.show()
