class Solution {
    public int maxProfit(int[] prices) {
        
        int[] maximumRight = new int[prices.length];
        int largest = 0;
        for (int i = prices.length-1; i > -1; i--) {
            largest = Math.max(largest, prices[i]);
            maximumRight[i] = largest;
        }

        int best = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            best = Math.max(best, maximumRight[i] - prices[i]);
        }
        return best;
    }
}