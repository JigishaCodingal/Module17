import scipy.stats as stats

# Number of trials and probability of success
n_flips = 10
p_success = 0.5

# Probability of observing exactly 3 heads: P(X = 3)
prob_exactly_3 = stats.binom.pmf(3, n_flips, p_success)

# Probability of observing more than 2 heads: P(X > 2) = 1 - P(X <= 2)
prob_more_than_2 = 1 - stats.binom.cdf(2, n_flips, p_success)

# Output results
print(f"Probability of observing exactly 3 heads: {prob_exactly_3:.4f}")
print(f"Probability of observing more than 2 heads: {prob_more_than_2:.4f}")
