int pivotIndex(int* nums, int numsSize) {
    int left = 0;
    int right = 0;
    for (int i = 1; i < numsSize; i++) {
        right += nums[i];
    }
    if (left == right) {
        return 0;
    }
    for (int i = 1; i < numsSize; i++) {
        left += nums[i-1];
        right -= nums[i];
        if (left == right) {
            return i;
        }
    }
    return -1;
}