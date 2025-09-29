class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        deque<int> q; // monotonic queue

        // maximum is at the front
        auto findMax = [&]() {
            return q.front();
        };

        // if elements in front are smaller, we can remove them
        auto enqueue = [&](int element) {
            while (!q.empty() && q.back() < element)
                q.pop_back();
            q.push_back(element);
        };

        // we only remove the front element if it matches
        // because we don't keep track of every element
        auto dequeue = [&](int element) {
            if (!q.empty() && q.front() == element)
                q.pop_front();
        };

        vector<int> result;

        // constant sliding window
        for (int i = 0; i < nums.size(); i++) {
            if (i >= k)
                dequeue(nums[i-k]);
            enqueue(nums[i]);
            if (i >= k - 1)
                result.push_back(findMax());
        }

        return result;
    }
};