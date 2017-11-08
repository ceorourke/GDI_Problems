def find_lonely_number_standard(nums):
    """Returns the number that only appears once using a dictionary"""

    num_counts = {}

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    for num in num_counts:
        if num_counts[num] == 1:
            return num

def find_lonely_number_fancy(nums):
    """Returns the number that appears only once using .count()"""

    for num in nums:
        if nums.count(num) == 1:
            return num

def find_lonely_number_comprehension(nums):
    """An alternate method to the above that uses a list comprehension"""

    result = [num for num in nums if nums.count(num) == 1]
    return result[0]

nums = [2,6,3,8,6,2,3]
print find_lonely_number_standard(nums)
print find_lonely_number_fancy(nums)
print find_lonely_number_comprehension(nums)