class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        stack<pair<int, int>> s1, s2;

        auto findMax = [&]() {
            if (s1.empty() || s2.empty())
                return s1.empty() ? s2.top().second : s1.top().second;
            else
                return max(s1.top().second, s2.top().second);
        };

        auto enqueue = [&](int element) {
            int maximum = s1.empty() ? element : max(element, s1.top().second);
            s1.push({element, maximum});
        };

        auto dequeue = [&]() {
            if (s2.empty()) {
                while (!s1.empty()) {
                    int element = s1.top().first;
                    s1.pop();
                    int maximum = s2.empty() ? element : max(element, s2.top().second);
                    s2.push({element, maximum});
                }
            }
            s2.pop();
        };

        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            if (i < k) {
                enqueue(nums[i]);
            } else {
                dequeue();
                enqueue(nums[i]);
            }
            if (i >= k - 1) {
                result.push_back(findMax());
            }
        }

        return result;
    }
};