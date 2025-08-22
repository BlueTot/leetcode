int maxVowels(char* s, int k) {
    int greatest = 0;
    int num_vowel = 0;
    char vowels[] = "aeiou";
    bool isvowel[strlen(s)];
    for (int i = 0; i < strlen(s) - k + 1; i++) {
        if (i == 0) {
            for (int j = 0; j < k; j++) {
                if (strchr(vowels, s[j]) != NULL) {
                    num_vowel++;
                    isvowel[j] = true;
                } else {
                    isvowel[j] = false;
                }
            }
        } else {
            if (isvowel[i-1]) {
                num_vowel--;
            }
            if (strchr(vowels, s[i+k-1]) != NULL) {
                num_vowel++;
                isvowel[i+k-1] = true;
            } else{
                isvowel[i+k-1] = false;
            }

        }
        if (num_vowel > greatest) {
            greatest = num_vowel;
        }
    }
    return greatest;
}