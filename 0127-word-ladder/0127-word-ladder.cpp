class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
        // calculate number of differences
        // sizes are the same
        auto num_differences = [](string a, string b) {
            int count = 0;
            for (int i = 0; i < a.size(); i++) {
                if (a[i] != b[i]) {
                    count++;
                }
            }
            return count;
        };

        // create the graph
        unordered_map<string, vector<string>> graph;
        for (int i = 0; i < wordList.size(); i++) {
            for (int j = i + 1; j < wordList.size(); j++) {
                if (num_differences(wordList[i], wordList[j]) == 1) {
                    graph[wordList[i]].push_back(wordList[j]);
                    graph[wordList[j]].push_back(wordList[i]);
                }
            }
        }

        for (string word : wordList) {
            if (num_differences(beginWord, word) == 1) {
                graph[beginWord].push_back(word);
                graph[word].push_back(beginWord);
            }
        }

        // for (auto pair : graph) {
        //     for (string value : pair.second) {
        //         cout << pair.first << " " << value << "\n";
        //     }
        // }

        // breadth-first-search
        unordered_set<string> visited;
        deque<pair<string, int>> queue;
        queue.push_back({beginWord, 0});
        visited.insert(beginWord);

        while (!queue.empty()) {
            auto [word, dist] = queue.front(); queue.pop_front();
            if (word == endWord) {
                return dist + 1;
            }
            for (string next : graph[word]) {
                if (!visited.contains(next)) {
                    visited.insert(next);
                    queue.push_back({next, dist + 1});
                }
            }
        }

        return 0;
    }
};