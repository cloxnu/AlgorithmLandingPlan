class Solution:
    def maxTurbulenceSize(self, arr: list) -> int:
        if len(arr) <= 1:
            return len(arr)
        elif len(arr) == 2:
            return 1 if arr[0] == arr[1] else 2
        last_num = arr[0]
        is_down = True
        max_count, curr_count = 1, 1
        for num in arr[1:]:
            if is_down and num > last_num or not is_down and num < last_num:
                curr_count += 1
            elif num == last_num:
                curr_count = 1
            else:
                curr_count = 2
            is_down = num < last_num
            last_num = num
            max_count = max(max_count, curr_count)
        return max_count
