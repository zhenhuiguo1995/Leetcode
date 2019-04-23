#### Edit Distance

Given two words *word1* and *word2*, find the minimum number of operations required to convert *word1* to *word2*.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

**Analysis:**

Use f(i, j) to represent the minimum number of operations to make str1[1:i] and str2[1:j] the same. Then we have:

-> f(i-1, j) represents the minimum number of operations to get str1[1:i-1] the same with str2[1:j], then we only need to delete str1[i] to make str[1:i] the same as str2[1:j] 

-> f(i, j - 1) represents the minimum number of operations to get str1[1:i] the same with str2[1:j - 1], then we only need to add str2[j] to str1[1:i] to get the same string as str2[1:j] 
$$
f(i, j) = min\begin{cases}
	\begin{cases}
		f(i-1, j-1), str1[i] == str2[j]\\
		f(i-1, j-1) + 1, str1[i] != str2[j]\\
	\end{cases}\\
	f(i-1, j) + 1\\
	f(i, j-1) + 1\\
\end{cases}
$$


 **Base case:**

f(i, 0) = i, f(0, j) = j



```java
class Solution {
    public int minDistance(String word1, String word2) {
        // deal with corner case
        if (word1 == null) return word2.length();
        if (word2 == null) return word1.length();
        
        // initialize variables
        int m = word1.length();
        int n = word2.length();
        int[][] dp = new int[m+1][n+1];
        for (int i = 0; i < m+1; i ++) dp[i][0] = i;
        for (int j = 0; j < n+1; j ++) dp[0][j] = j;
        // fill dp matrix
        for (int i = 1; i < m+1; i ++) {
            for (int j = 1; j < n+1; j ++) {
                if (word1.charAt(i-1) == word2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                dp[i][j] = Math.min(
                    Math.min(dp[i][j], dp[i-1][j] + 1), dp[i][j-1] + 1);
            }
        }
        return dp[m][n];
    }
}
```

