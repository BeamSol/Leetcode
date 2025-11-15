int numberOfSubstrings(string s) {
    int len = s.size();
    //2 seperate prefix sums for 1s and 0s counts to simplify the explanation
    vector<int> pref0(len);
    vector<int> pref1(len);
    pref0[0] = s[0] == '0';
    pref1[0] = s[0] == '1';
    for (int i = 1; i < len; i++) {
        pref0[i] = pref0[i - 1] + (s[i] == '0');
        pref1[i] = pref1[i - 1] + (s[i] == '1');
    }

   // we will focus in this nested loop
    int count = 0;
    for (int i = 0; i < len; i++) {
        for (int j = i; j < len; j++) {
            int zeros = pref0[j] - (i ? pref0[i - 1] : 0);
            int ones = pref1[j] - (i ? pref1[i - 1] : 0);

            if (ones >= zeros * zeros)
                count++;
            
        }
    }
    return count;
}