import scipy.stats as stats

# Given parameters
lambda_calls = 15

# Probability of observing more than 20 calls: P(X > 20) = 1 - P(X <= 20)
prob_more_than_20 = 1 - stats.poisson.cdf(20, lambda_calls)

# Probability of observing between 17 and 21 calls: P(17 <= X <= 21) = P(X <= 21) - P(X <= 16)
prob_between_17_21 = stats.poisson.cdf(21, lambda_calls) - stats.poisson.cdf(16, lambda_calls)

# Output results
print(f"Probability of observing more than 20 calls: {prob_more_than_20:.4f}")
print(f"Probability of observing between 17 and 21 calls: {prob_between_17_21:.4f}")
