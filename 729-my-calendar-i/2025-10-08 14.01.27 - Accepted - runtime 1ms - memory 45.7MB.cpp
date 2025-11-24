class MyCalendar {
public:

    vector<vector<int>> intervals;

    MyCalendar() {
        
    }
    
    bool book(int startTime, int endTime) {
        int left = 0;
        int right = intervals.size(); // we can insert after.
        int mid;
        while (left < right) {
            mid = (left + right) / 2;
            if (intervals[mid][0] > startTime)
                right = mid;
            else
                left = mid + 1;
        }

        // we now have the two concerning intervals at left-1 and left.
        // insert at start
        if (left == 0) {
            if (intervals.size() == 0 || intervals[left][0] >= endTime) {
                intervals.emplace(intervals.begin() + left, vector<int>{startTime, endTime});
                return true;
            }
            return false;
        // insert at end
        } else if (left == intervals.size()) {
            if (intervals.size() == 0 || startTime >= intervals[left-1][1]) {
                intervals.emplace(intervals.begin() + left, vector<int>{startTime, endTime});
                return true;
            }
            return false;
        // insert in middle
        } else if (intervals[left-1][1] <= startTime && endTime <= intervals[left][0]) {
            intervals.emplace(intervals.begin() + left, vector<int>{startTime, endTime});
            return true;
        } else {
            return false;
        }
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */