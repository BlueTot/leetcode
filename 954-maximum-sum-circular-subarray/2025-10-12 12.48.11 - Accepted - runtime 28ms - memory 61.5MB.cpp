class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        
        // we do a prefix sum over the doubled array
        vector<long long> prefix(nums.size() * 2 + 1, 0);
        prefix[0] = 0;
        for (int i = 0; i < nums.size() * 2; i++) {
            prefix[i+1] = prefix[i] + nums[i % nums.size()];
        }


        // monotonic queue operations
        deque<pair<long long, int>> mqueue;

        auto getMin = [&]() {
            return mqueue.front();
        };

        auto enqueue = [&](pair<long long, int> value) {
            while (!mqueue.empty() && mqueue.back().first > value.first)
                mqueue.pop_back();
            mqueue.push_back(value);
        };

        auto dequeue = [&](int first) {
            if (!mqueue.empty() && mqueue.front().first == first)
                mqueue.pop_front();
        };

        long long maximum = 1 << 31;
        long long current;
        enqueue({0, -1});

        for (int i = 0; i < 2 * nums.size(); i++) {
            
            // remove all invalid prefix sums
            while (!mqueue.empty() && (getMin().second < i - (int) nums.size())) {
                dequeue(getMin().first);
            }

            current = prefix[i+1] - getMin().first;
            maximum = max(maximum, current);

            enqueue({prefix[i+1], i});
        } 

        return maximum;

    }
};