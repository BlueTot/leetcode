#include <iostream>
#include <string>

class Solution {
public:
    int findNthDigit(int n) {
        
        // find the starting index of a given number in the integer sequence
        auto findIndex = [&](int n) {

            int num_digits = floor(log10(n)) + 1;

            // find the number of digits before num_digits.
            // pattern is 9, 90*2, 900*3, ...
            // = 9, 9(10)(2), 9(10^2)(3), ...
            long long result = 1;
            for (int i = 1; i < num_digits; i++) {
                result += 9LL * (int) pow(10, i-1) * i;
            }

            // add on the remaining gap
            result += (n - (long long) pow(10, num_digits - 1)) * num_digits;

            return result;
        };

        int left = 1;
        int right = 1 << 30;
        int mid;
        
        // find the smallest value with findIndex > n.
        while (left < right) {
            mid = (left + right) / 2;
            if (findIndex(mid) > (long long) n)
                right = mid;
            else
                left = mid + 1;
        }
        
        int start_number = left - 1;
        int remaining = n - findIndex(start_number);
        return to_string(start_number).at(remaining) - '0';

        return 0;
    }
};