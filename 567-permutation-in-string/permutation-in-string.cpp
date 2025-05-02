class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        
        unordered_map<char, int> origFreq;
        for (const auto& c : s1) {
            origFreq[c]++;
        }
        unordered_map<char, int> freq;
        int left = 0;
        int formed = 0;
        size_t required = origFreq.size();

        for (int right = 0; right < s2.length(); right++) {
            freq[s2[right]]++;

            if (freq[s2[right]] == origFreq[s2[right]])
                formed++;
            
            while (left <= right && formed == required) {
                if (origFreq == freq)
                    return true;

                if (origFreq[s2[left]] > 0 && origFreq[s2[left]] == freq[s2[left]])
                    formed--;
                freq[s2[left]]--;
                left++;
            }

        }
        return false;


    }
};