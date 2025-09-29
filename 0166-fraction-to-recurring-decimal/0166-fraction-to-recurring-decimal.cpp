class Solution {
public:
    string fractionToDecimal(int numerator_int, int denominator_int) {

        // edge case
        if (numerator_int == 0)
            return "0";
        
        bool sign = (numerator_int >= 0) ^ (denominator_int >= 0);      
        long long numerator = std::abs((long long) numerator_int);
        long long denominator = std::abs((long long) denominator_int);

        std::unordered_map<long long, int> numerators;
        std::vector<long long> digits;
        int index = 0;
        bool is_fractional = numerator < denominator;

        // we only store the numerator if we've entered the fractional part
        // used to fix bug where repeating starts recording from non-fractional part
        if (is_fractional)
            numerators[numerator] = index;

        int repeat_length = 0;
        while (numerator > 0) {
            if (numerator >= denominator) {
                digits.push_back(numerator / denominator);
                numerator %= denominator;
            } else {
                digits.push_back(0);
            }
            numerator *= 10;
            if (numerators.contains(numerator)) {
                // std::cout << numerators[numerator] << " " << index << "\n";
                // std::cout << numerator << "\n";
                repeat_length = index - numerators[numerator];
                break;
            }
            if (is_fractional || index >= 1)
                numerators[numerator] = index;
            index++;
            // for (int digit : digits) {
            //     std::cout << digit << ", ";
            // }
            // std::cout << "\n";
            // std::cout << is_fractional << "\n";
        }

        // for (int digit : digits) {
        //     std::cout << digit << ", ";
        // }
        // std::cout << digits.size() << "\n";

        stringstream s;
        int i;

        // insert the sign
        if (sign) s << "-";

        for (i = 0; i < digits.size() - repeat_length; i++) {
            s << digits[i];
            if (i == 0 && digits.size() > 1)
                s << ".";
        }
        if (i < digits.size()) {
            s << "(";
            for (int j = i; j < digits.size(); j++) {
                s << digits[j];
            }
            s << ")";
        }
        return s.str();
    }
};