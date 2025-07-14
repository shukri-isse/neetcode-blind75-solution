# Brute force solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False

# Hash set solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create an empty hashset
        hashset = set()
        #loop through every number in int array nums
        for num in nums:
            # if number is aldready in hashset it is a duplicate
            if num in hashset:
                #if it is it's a duplicate and return now and exit function
                return True
            #add to hashset only if false and not a duplicate
            hashset.add(num)
        # if we go through the entire list and dont find a duplicate, return false
        return False