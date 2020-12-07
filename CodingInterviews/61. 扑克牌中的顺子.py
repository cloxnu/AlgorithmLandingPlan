def isStraight(nums: list) -> bool:
    without0 = list(filter(lambda a: a, nums))
    return len(without0) == len(set(without0)) and max(nums) - min(without0) <= 4


print(isStraight([2, 3, 0, 4, 0, 8]))
