int largestAltitude(int* gain, int gainSize) {
    int max_altitude = 0;
    int altitude = 0;
    for (int i = 0; i < gainSize; i++) {
        altitude += gain[i];
        if (i == 0 || altitude > max_altitude) {
            max_altitude = altitude;
        }
    }
    if (max_altitude < 0) {
        return 0;
    }
    return max_altitude;
}