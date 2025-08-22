// #include <strlib.h>

bool isSubsequence(char* s, char* t) {
    if (strlen(s) == 0) {
        return true;
    }
    int j = 0;
    for (int i = 0; i < strlen(t); i++) {
        if (t[i] == s[j]) {
            j++;
        }
        if (j == strlen(s)) {
            return true;
        }
    }
    return false;
}