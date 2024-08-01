
class Solution:
    def maxElement(self, mat, mid):
        """
        Find the row index of the maximum element in the given column (mid).
        """
        maxValue = -1  # Initialize the maximum value found in the column
        index = -1  # Initialize the row index of the maximum value
        for i in range(len(mat)):
            if mat[i][mid] > maxValue:
                maxValue = mat[i][mid]
                index = i
        return index

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        Find a peak element in a 2D grid where a peak element is greater than its neighbors.
        """
        low = 0
        high = len(mat[0]) - 1  # Initialize high to the last column index

        while low <= high:
            mid = low + (high - low) // 2  # Calculate the middle column
            row = self.maxElement(mat, mid)  # Find the row with the maximum element in the middle column

            # Check the left neighbor
            if mid - 1 >= 0:
                left = mat[row][mid - 1]
            else:
                left = -1  # If the left neighbor is out of bounds, treat it as -1

            # Check the right neighbor
            if mid + 1 < len(mat[0]):
                right = mat[row][mid + 1]
            else:
                right = -1  # If the right neighbor is out of bounds, treat it as -1

            # Check if the middle element is greater than both left and right neighbors
            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]  # Return the position if it's a peak
            elif mat[row][mid] < left:
                high = mid - 1  # Move the search to the left half if the left neighbor is greater
            else:
                low = mid + 1  # Move the search to the right half if the right neighbor is greater


# O(mlogn) TC
# O(1) SC