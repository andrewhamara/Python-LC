# Author: Andrew Hamara

# Solution to leetcode problem 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote:str, magazine:str) -> bool:
        for val in set(ransomNote):
            if ransomNote.count(val) > magazine.count(val):
                return False
        return True
