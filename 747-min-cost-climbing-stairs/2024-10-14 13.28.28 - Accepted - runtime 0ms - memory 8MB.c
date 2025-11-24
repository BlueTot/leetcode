int min(int a, int b) {
    if (a > b) {
        return b;
    } else {
        return a;
    }
}

int minCostClimbingStairs(int* cost, int costSize) {
    int runningCosts[costSize+1];
    runningCosts[0] = 0;
    runningCosts[1] = 0;
    for (int i = 2; i < costSize+1; i++) {
        runningCosts[i] = min(runningCosts[i-2] + cost[i-2], runningCosts[i-1] + cost[i-1]);
    }
    return runningCosts[costSize];
}