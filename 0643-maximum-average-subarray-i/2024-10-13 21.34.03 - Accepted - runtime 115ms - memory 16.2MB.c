double findMaxAverage(int* nums, int numsSize, int k) {
    int greatest = 0;
    int moving_average = 0;
    // int i = 0;
    // int j = 0;
    // while (j < numsSize) {
    //     if (j < k) {
    //         moving_average += nums[j];
    //         if (j == k - 1) {
    //             i++;
    //             greatest = moving_average;
    //         }
    //         j++;
    //     } else {
    //         moving_average -= nums[i-1];
    //         moving_average += nums[j];
    //         i++;
    //         j++;
    //         if (moving_average > greatest) {
    //             greatest = moving_average;
    //         }
    //     }
    //     // printf("%d %d\n", i, j);
         
    // }
    for (int i = 0; i < numsSize - k + 1; i++) {
        if (i == 0) {
            for (int j = 0; j < k; j++) {
                moving_average += nums[j];
            }
        } else {
            moving_average -= nums[i-1];
            moving_average += nums[i+k-1];
        }
        if (moving_average > greatest || i == 0) {
            greatest = moving_average;
        }  
    }
    return ((double) greatest) / ((double) k);
}