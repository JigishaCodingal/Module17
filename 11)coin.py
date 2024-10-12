import java.math.BigInteger;

public class CoinFlipProbability {

    // Method to calculate factorial of a number
    public static BigInteger factorial(int n) {
        BigInteger result = BigInteger.ONE;
        for (int i = 2; i <= n; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }

    // Method to calculate binomial coefficient nCk
    public static BigInteger binomialCoefficient(int n, int k) {
        return factorial(n).divide(factorial(k).multiply(factorial(n - k)));
    }

    // Method to calculate the probability of exactly k heads in n flips
    public static double calculateProbability(int n, int k, double p) {
        BigInteger binomialCoeff = binomialCoefficient(n, k);
        return binomialCoeff.doubleValue() * Math.pow(p, k) * Math.pow(1 - p, n - k);
    }

    public static void main(String[] args) {
        int n = 10; // Number of coin flips
        int k = 3;  // Number of heads we want to observe
        double p = 0.5; // Probability of heads on each flip

        double probability = calculateProbability(n, k, p);
        System.out.printf("The probability of observing exactly %d heads in %d flips is: %.5f\n", k, n, probability);
    }
}
