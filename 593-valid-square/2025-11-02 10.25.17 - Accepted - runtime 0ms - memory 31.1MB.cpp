class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {

        vector<vector<int>> points = {p1, p2, p3, p4};

        auto v = [&](int i, int j) {
            return vector<int>{points[i][0] - points[j][0], points[i][1] - points[j][1]};
        };

        vector<vector<int>> vectors = {v(0, 1), v(0, 2), v(0, 3), v(1, 2), v(1, 3), v(2, 3)};

        auto square = [](int x) {
            return (long long) x * x;
        };

        auto magn2 = [&](const vector<int>& a) {
            return (long long) square(a[0]) + (long long ) square(a[1]);
        };

        auto dot = [&](const vector<vector<int>>& vs, int i, int j) {
            return vs[i][0] * vs[j][0] + vs[i][1] * vs[j][1];
        };

        unordered_set<long long> magnitudes;
        for (auto vector : vectors) {
            magnitudes.insert(magn2(vector));
        }

        if (magnitudes.size() != 2)
            return false;
        
        long long best = numeric_limits<long long>::max();
        for (long long num : magnitudes)
            best = min(best, num);
        
        vector<vector<int>> vs;
        for (const vector<int>& v : vectors) {
            if (magn2(v) == best)
                vs.push_back(v);
        }

        if (vs.size() != 4)
            return false;

        vector<vector<int>> pairs = {{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}};
        for (const vector<int>& pair : pairs) {
            long long d = (long long) dot(vs, pair[0], pair[1]);
            long long maximum = (long long) magn2(vs[pair[0]]) * magn2(vs[pair[1]]);
            if (d != 0 && d * d != maximum) {
                return false;
            }
        }

        return true;

    }
};