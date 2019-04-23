#### Longest Palindrome Substring

**Description:** Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

**Analysis:** the goal in this question is to get the longest palindrome substring, however it is most convenient of us to record if a substring is a palindrome. Therefore we need to global variables to record the start and end position of s palindrome substring, and the dp matrix represents s.substring(i, j) is a palindrome string or not.

**State transition function:**
$$
f(i, j) = \begin{cases}
	f(i + 1, j - 1)  \&   s[i] == s[j], i <j - 2 \\
	s[i] == s[j], i = j + 1
\end{cases}
$$
**Base case**:

the diagonal of the do matrix should be filled with true, f(i, i) = true.

And when i > j, the substring does not exist, therefore we only need to consider cases i <= j.

```java
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return "";
        int start = 0;
        int end = 0;
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i ++) {
            dp[i][i] = true;
        } 
        for (int i = n-1; i >= 0; i --) {
            for (int j = i; j < n; j ++) {
                if (i + 1 <= j - 1) {
                    dp[i][j] = dp[i+1][j-1] && (s.charAt(i) == s.charAt(j));
                    if (dp[i][j] && j - i > end - start) {
                        start = i;
                        end = j;
                    }
                } else {
                    dp[i][j] = (s.charAt(i) == s.charAt(j));
                    if (dp[i][j] && j - i > end - start) {
                        start = i;
                        end = j;
                    }
                }
            }
        }
        //System.out.println(start);
        //System.out.println(end);
        return s.substring(start, end + 1);
    }
}
```

**Note:** since s.substring(i, j) = s[i:j), we need to return s.substring(start, end + 1)