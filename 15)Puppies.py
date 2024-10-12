import numpy as np

# Define parameters
total_puppies = 10000
sample_size = 20
blue_eyed_proportion = 0.4  # Assuming 40% of puppies have blue eyes

# Simulate the sample of puppies (1 for blue eyes, 0 for hazel eyes)
# Use np.random.choice to create a sample
sample = np.random.choice(
    [1, 0],  # Possible outcomes (1 for blue eyes, 0 for hazel eyes)
    size=sample_size,  # Sample size
    p=[blue_eyed_proportion, 1 - blue_eyed_proportion]  # Probabilities
)

# Calculate the proportion of blue-eyed puppies in the sample
blue_eyed_count = np.sum(sample)
proportion_blue_eyed = blue_eyed_count / sample_size

# Output results
print(f"Sample of puppies' eye colors: {sample}")
print(f"Number of blue-eyed puppies in sample: {blue_eyed_count}")
print(f"Proportion of blue-eyed puppies in sample: {proportion_blue_eyed:.2f}")
