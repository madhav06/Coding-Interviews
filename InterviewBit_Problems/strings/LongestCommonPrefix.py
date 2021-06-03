# Given the array of strings A,
# you need to find the longest string S which is the prefix of ALL the strings in the array.

# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
# and S2.

# For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

# Input 1:
#     A = ["abcdefgh", "aefghijk", "abcefgh"]
# Output 1:
#     "a"
#     Explanation 1:
#         Longest common prefix of all the strings is "a".

# Input 2:
#     A = ["abab", "ab", "abcd"];
# Output 2:
#     "ab"
#     Explanation 2:
#         Longest common prefix of all the strings is "ab".

class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, words):
        min_word = min(words, key=lambda word: len(word))
        n = len(min_word)
        m = len(words)
        
        for i in range(n):
            for j in range(m):
                if words[j][i] != min_word[i]:
                    return min_word[:i]

        return min_word