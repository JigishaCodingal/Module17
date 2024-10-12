import scipy.stats as stats

# Number of trials and probability of success
n_flips = 10
p_success = 0.5

# Probability of observing more than 6 heads: P(X > 6) = 1 - P(X <= 6)
prob_more_than_6 = 1 - stats.binom.cdf(6, n_flips, p_success)

# Output result
print(f"Probability of observing more than 6 heads: {prob_more_than_6:.4f}")
