# Python Program for recursive binary search.
# The idea of binary search is to use the information that the array *is sorted*
# and reduce the time complexity (worst case) to O(Log n).
# n/(2^k) <= 1; n <= 2^k; k = log2n

# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

import unittest

class Test(unittest.TestCase):
    def test_binarysearch(self):
        # Test array
        arr = [2, 3, 4, 10, 40]
        x = 10
        expectedresult = 3
        result = binarySearch(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, expectedresult)

if __name__ == "__main__":
    unittest.main()
