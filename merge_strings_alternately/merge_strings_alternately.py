class Solution:
    def __init__(self):
        pass

    def mergeAlternately(self, word1: str, word2: str) -> str:
        # String result
        result = ""
        # Get substring > word1 max length
        rest = word2[len(word1)::]
        # Calculate max index for iteration purposes
        maxIndex = len(word2) - 1
        # Iterate over word1 to mix words
        for i, value in enumerate(word1):
            # Append current value to result
            result += value
            # If index exist on word2 append value to result, else skip
            if (i <= maxIndex):
                result += word2[i]
        # return value and append missing iterated words
        return result + rest


"""test = Solution().mergeAlternately("ab", "pqrs")
print(f'Expected: apbqrs \nResult {test}')"""
