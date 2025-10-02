class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        
        int drunk = numBottles;
        int empty = numBottles;
        while (empty >= numExchange) {
            empty -= numExchange;
            numExchange++;
            empty += 1;
            drunk += 1;
        }
        return drunk;
        
    }
};