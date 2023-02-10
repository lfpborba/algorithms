def find_duplicate(nums):
    if not is_valid_list(nums):
        return False
    nums_set = set()

    for num in nums:
        if num in nums_set:
            return num
        nums_set.add(num)

    return False


def is_valid_list(nums):
    if not nums or type(nums) != list or len(nums) < 2:
        return False

    for num in nums:
        if type(num) != int or num < 1:
            return False

    return True
