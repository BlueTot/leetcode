class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {

        // precompute primes up to 10**5.
        int n = 100000;
        vector<bool> is_prime(n+1, true);
        is_prime[0] = is_prime[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (is_prime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    is_prime[j] = false;
                }
            }
        }

        // determine number of divisors and sum of divisors
        // d(n) = (a1 + 1)(a2 + 1)...(an + 1) where n = p^a1 * p^a2 * ... * p^an
        // so for d(n) = 4, we must have either a1 = 1, a2 = 1 (two prime factors)
        // or a1 = 3 (one prime factor)

        auto hasFourDivisors = [&](int num, int& sum) {

            // num = p * q
            for (int p = 2; p * p <= n; p++) {
                if (!is_prime[p]) continue;
                if (num % p == 0) {
                    int q = num / p;
                    if (p != q && is_prime[q]) {
                        sum = 1 + p + q + p * q;
                        return true;
                    }
                }
            }

            // num = p * p * p
            int root = round(pow(num, 1.0/3));
            if ((long long) root * root * root == num && is_prime[root]) {
                sum = 1 + root + root * root + num;
                return true;
            }

            return false;
        };

        int result = 0;
        for (int num : nums) {
            int sum = 0;
            if (hasFourDivisors(num, sum))
                result += sum;     
        }

        return result;

    }
};