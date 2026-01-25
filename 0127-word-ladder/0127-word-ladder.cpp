class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {

        // make set of words
        unordered_set<string> words;
        for (string word : wordList)
            words.insert(word);

        unordered_set<string> visited;
        deque<pair<string, int>> queue;
        queue.push_back({beginWord, 0});
        visited.insert(beginWord);
        string next;

        // breadth-first-search
        // time complexity is O(N * L)

        while (!queue.empty()) {
            auto [word, dist] = queue.front(); queue.pop_front();
            if (word == endWord) {
                return dist + 1;
            }

            // on each iteration, finding neighbours is O(26 * L)
            // which is O(L)
            for (int i = 0; i < word.size(); i++) {
                for (char c = 'a'; c <= 'z'; c++) {
                    next = word; // copy
                    next = next.replace(i, 1, 1, c);
                    if (words.contains(next) && !visited.contains(next)) {
                        visited.insert(next);
                        queue.push_back({next, dist + 1});
                    }
                }
            }
        }

        return 0;
    }
};