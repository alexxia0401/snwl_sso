#!/usr/bin/python3

# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        usedChar = {}
        start = 0
        maxLen = 0
        for idx, value in enumerate(s):
            if value in usedChar and start <= usedChar[value]:
                start = usedChar[value] + 1
            else:
                maxLen = max(maxLen, idx - start + 1)

            usedChar[value] = idx
        return maxLen

if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLongestSubstring('abcabcbb'))
    print(test.lengthOfLongestSubstring('bbbbb'))
    print(test.lengthOfLongestSubstring('pwwkew'))
    print(test.lengthOfLongestSubstring('tmmzuxt'))
