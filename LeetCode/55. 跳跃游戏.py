class Solution:
    def canJump(self, nums: list) -> bool:
        if len(nums) == 0:
            return True
        queue = [0]
        while queue:
            pos = queue.pop(0)
            if pos >= len(nums) - 1:
                return True
            maxJumpCount = nums[pos]
            for i in range(maxJumpCount):
                queue.append(pos + i + 1)
        return False

    def canJump2(self, nums: list) -> bool:
        if len(nums) <= 1:
            return True
        for idx in reversed(range(len(nums) - 1)):
            if nums[idx] == 0:
                for i in reversed(range(idx)):
                    if nums[i] > idx - i:
                        break
                else:
                    return False
        return True
