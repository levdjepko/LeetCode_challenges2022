import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    #  words = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']
    # This is mostly a sorted array with a rotation point somewhere in the middle
    # We will use a binary search to find the rotation point effectively
    
    left = 0
    right = len(words) - 1
    
    first_letter = words[0]
    
    while (left < right):
        # left ------ middle -----right
        middle = left + (right - left) // 2
        
        if words[middle] >= first_letter:
            left = middle
        else:
            right = middle
        
        # did we find the point?
        if left + 1 == right:
            return right

    return -1


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
