#### Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



**Analysis:**

We use dp[i] to record the maximum value ending at the ith element.
$$
dp[i] = max(dp[i - 1] + nums[i], nums[i])
$$
**Base case:** $dp[0] = nums[0]$

Then we get the max value in the dp array, which is the largest sum of all possible subarray

```java
class Solution {
    public int maxSubArray(int[] nums) {
        // dp[i] max subarray value ending at the ith element
        // corner case
        if (nums.length == 1) {
            return nums[0];
        }
        // initilization
        int[] dp = new int[nums.length];
        int max = nums[0];
        dp[0] = nums[0];
        // iteration
        for (int i = 1; i < nums.length; i ++) {
            dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
            max = Math.max(max, dp[i]);
        }
        return max;
        
    }
}
```

