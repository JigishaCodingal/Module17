import scipy.stats as stats

# Given lambda (expected value) for the Poisson distribution
lambda_rain = 10

# Probability of exactly 6 days of rain: P(X = 6)
prob_exactly_6 = stats.poisson.pmf(6, lambda_rain)

# Probability of 12 to 14 days of rain: P(12 <= X <= 14)
prob_12_to_14 = stats.poisson.cdf(14, lambda_rain) - stats.poisson.cdf(11, lambda_rain)

# Output results
print(f"Probability of exactly 6 days of rain: {prob_exactly_6:.4f}")
print(f"Probability of 12 to 14 days of rain: {prob_12_to_14:.4f}")
