class Solution:
    def is_unique(self, string):
        unique = set()

        for i in string:
            if i in unique:
                return False
            unique.add(i)
        return True

    def is_unique_by_bit(self, string):
        initial_bit = 0
        for i in string:
            # get ascii position and substract the first position to avoid working
            # with big numbers, this give us 1, 2... n position
            position =  ord(i) - ord('a')
            # this is and operator bit by bit and return 1 in binary if bit in position is
            # already 1, else return 0
            if (initial_bit & (1<< position)) > 0:
                return False
            initial_bit |= (1<< position)
        return True
    def n_log(self,string):
        # to have n log n runtime
        # log n means ordered data or divisions
        # sorted() takes n log n
        sorted_data = sorted(string)
        # -1 to avoid second pointer overflow
        for i in range(len(sorted_data) - 1):
            if(sorted_data[i] == sorted_data[i+1]):
                return False
        return True


if __name__ == "__main__":
    result = Solution()
    print(result.is_unique("pepe"))
    print(result.is_unique("hola"))

    print(result.is_unique_by_bit("pepe"))
    print(result.is_unique_by_bit("hola"))

    print(result.n_log("pepe"))
    print(result.n_log("hola"))
