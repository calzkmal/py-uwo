from collections import Counter

class Test:
    def canConstruct(self, ransomNote, magazine):
        a, b = Counter(ransomNote), Counter(magazine)
        return a & b == a

tes = Test()

print(tes.canConstruct("abc", "bca"))