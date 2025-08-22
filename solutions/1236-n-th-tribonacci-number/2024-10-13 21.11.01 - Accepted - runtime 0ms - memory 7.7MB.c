

int tribonacci(int n){
    if (n == 0) {
        return 0;
    } else if (n == 1 || n == 2) {
        return 1;
    }
    int a = 0;
    int b = 1;
    int c = 1;
    for (int i = 0; i < n - 2; i++) {
        int new = a + b + c;
        a = b;
        b = c;
        c = new;
    }
    return c;
}