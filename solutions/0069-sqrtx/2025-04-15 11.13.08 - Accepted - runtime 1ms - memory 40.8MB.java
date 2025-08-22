class Solution {
    public int mySqrt(int x) {
        
        int left = 0;
        int right = x;
        int mid;
        long square;
        
        while (left <= right) {

            mid = (left + right) / 2;
            square = (long) mid * mid;
            if (x == square) {
                return mid;
            } else if (x < square) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
        }
        return left - 1;
    }
}