
def majorityElement(self, nums: list) -> int:
    last, value = 0, 0
    for num in nums:
        if value == 0:
            last = num
            value += 1
        else:
            value += 1 if last == num else -1
    return last
