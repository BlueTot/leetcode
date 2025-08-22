int maxArea(int* height, int heightSize) {
    int start = 0;
    int end = heightSize - 1;
    int greatestArea = 0;
    int area = 0;
    while (start != end) {
        area = (end - start) * (height[start] > height[end] ? height[end] : height[start]);
        if (area > greatestArea) {
            greatestArea = area;
        }
        if (height[end] > height[start]) {
            start += 1;
        } else {
            end -= 1;
        }
    }
    return greatestArea;
}