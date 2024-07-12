class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dict = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in dict and dict[s[right]] >= left:
                left = dict[s[right]] + 1
            dict[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

s = "abcabcbb"

a = Solution()
print(a.lengthOfLongestSubstring(s)) 
