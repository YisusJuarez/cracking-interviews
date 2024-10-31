class Solution:
    def check_permutation(self, word1, word2):
        if len(word1) != len(word2):
            return False

        # Use hashtable to se word repetitions
        hashmap = {}
        for i in word1:
            if hashmap.get(i):
                hashmap[i] = hashmap[i] + 1
            else:
                hashmap[i] = 1

        for j in word2:
            if hashmap.get(j):
                hashmap[j] = hashmap[j] - 1
            else:
                return False
        return True

    def using_ascii(self, word1, word2):
        if len(word1) != len(word2):
            return False
        arrMap = [0]*128
        for i in word1:
            letter = ord(i)
            arrMap[letter] = arrMap[letter] + 1

        for j in word2:
            letter = ord(j)
            arrMap[letter] = arrMap[letter] - 1
            if arrMap[letter] < 0:
                return False
        return True

if __name__ == "__main__":
    print("...")
    result = Solution()
    print(result.check_permutation("hola", "holay"))
    print(result.using_ascii("aloh1", "hola"))
