#### Decode ways

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given a **non-empty** string containing only digits, determine the total number of ways to decode it.



**Analysis:**

1.First we need to build a hash map to record the decoding information

Use f(i) to represent the number of ways to decode the string s[1:i]
$$
f(i) = sum\begin{cases}
	f(i-1), Decodable(s[i])\\
	f(i-2), Decodable(s[i-1], i)
\end{cases}
$$
**Base case**

f(1) = decodable(s[1])

f(2) = decodable(s[1]) + decodable(s[1:2])



```java
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) return 0;
        // initializa a hashmap
        Map<String, Character> map = new HashMap<>();
        buildMap(map);
        // initialize dp matrix with base case
        int[] dp = new int[s.length()];
        dp[0] = map.containsKey(s.substring(0, 1)) ? 1 : 0;
        for (int i = 1; i < s.length(); i ++) {
            // parse separetely
            if (map.containsKey(s.substring(i, i+1))) {
                dp[i] += dp[i-1];
            }
            if (map.containsKey(s.substring(i-1, i+1))) {
                if (i == 1) dp[i] += 1;
                else dp[i] += dp[i-2];
            }
        }
        return dp[s.length()-1];
    }
    
    // pay attention to the parameter passed in
    public void buildMap(Map<String, Character> map) {
        map.put("1", 'A');
        map.put("2", 'B');
        map.put("3", 'C');
        map.put("4", 'D');
        map.put("5", 'E');
        map.put("6", 'F');
        map.put("7", 'G');
        map.put("8", 'H');
        map.put("9", 'I');
        map.put("10", 'J');
        map.put("11", 'K');
        map.put("12", 'L');
        map.put("13", 'M');
        map.put("14", 'N');
        map.put("15", 'O');
        map.put("16", 'P');
        map.put("17", 'Q');
        map.put("18", 'R');
        map.put("19", 'S');
        map.put("20", 'T');
        map.put("21", 'U');
        map.put("22", 'V');
        map.put("23", 'W');
        map.put("24", 'X');
        map.put("25", 'Y');
        map.put("26", 'Z');
    }
    
    
}
```

