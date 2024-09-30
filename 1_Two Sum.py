class Solution:
    def twoSum(self, nums, target):
        d = {}  # Dictionary to store the number and its index
        for i, x in enumerate(nums):  # Loop over the list with index and value
            y = target - x  # Calculate the complement
            if y in d:  # Check if the complement exists in the dictionary
                return [d[y], i]  # Return the indices if a match is found
            d[x] = i  # Add the number and its index to the dictionary
