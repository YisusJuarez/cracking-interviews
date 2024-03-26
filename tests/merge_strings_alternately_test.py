import unittest
from merge_strings_alternately.merge_strings_alternately import Solution


class TestMergeStringsAlternately(unittest.TestCase):
    def test_case_1(self):
        solution = Solution().mergeAlternately('abc', 'def')
        self.assertEqual(solution, "adbecf", "Should mix both strings")

    def test_case_2(self):
        solution = Solution().mergeAlternately('ab', 'pqrs')
        self.assertEqual(solution, "apbqrs", "Should mix both strings")


if __name__ == '__main__':
    unittest.main()
