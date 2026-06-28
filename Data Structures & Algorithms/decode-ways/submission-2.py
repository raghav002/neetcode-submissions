class Solution:
    def numDecodings(self, s: str) -> int:
        # String of upper case can be encoded
        # A= "1", Z = "26"
        # Decoding -> Group digits then map back into letters using
        # reverse mapping above. Multiple ways to decode a message
        # "1012" can be "JAB", "JL"
        # 1 01 2 invalid; 1 0 1 2 invalid because 0 cannot be mapped
        # If something has a leading 0 -> Invalid
        # Given a string s containing digits, return num ways to decode it
        # So, at max, we can decode only 2 digits. At min, 1 digit
        # So, at every i within the string, we choose either to decode this 
        # digit separately from the previous ones or together with the previous
        # one
        # if dp[i] indicates the number of ways to decode the message until
        # the ith point
        # dp[i] = 
        # Decode this digit separately from previous i-1 digits
        # dp[i-1]
        # Decode this digit together with previous digit 
        # dp[i-2] 
        # So:
        # dp[i] = dp[i-1] + dp[i-2]
        n = len(s)
        dp = [0]*n

        if n == 1:
            if s[0]=='0':
                return 0
            else:
                return 1

        # Base case 1: 
        if s[0]!='0':
            dp[0] = 1
        else:
            dp[0] = 0
        if s[1]!='0':
            dp[1] += dp[0]
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1
        for i in range(2, n):
            if s[i]!='0':
                dp[i] = dp[i] + dp[i-1]
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1])>=10:
                dp[i] = dp[i] + dp[i-2]
        return dp[n-1]
        