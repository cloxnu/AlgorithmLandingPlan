from itertools import accumulate


class State:
    def __init__(self, left=None, right=None, suffix_link=None):
        self.left = left
        self.right = right
        self.suffix_link = suffix_link
        self.transition = {}


class STree:
    def __init__(self):
        self.string = ""
        self.end_idxes = []
        self.auxiliary = State()  # the auxiliary state ⊥
        self.root = State(-1, -1, self.auxiliary)

    def build(self, string, end_idxes=None):
        self.string = string
        self.end_idxes = end_idxes if end_idxes else []
        self.auxiliary = State()  # the auxiliary state ⊥
        self.root = State(-1, -1, self.auxiliary)
        for char in self.string:
            self.auxiliary.transition[char] = self.root
        active_state = self.root
        left = 0
        for idx in range(len(self.string)):
            active_state, left = self._update(active_state, left, idx)
            active_state, left = self._canonize(active_state, left, idx)
        if self.end_idxes:
            self.root.transition['end'] = State(self.end_idxes[-1], float("inf"))

    def build_with_automatic_end(self, strings):
        string = '$'.join(strings) + '$'
        end_idxes = list(accumulate(strings, lambda x, y: x + len(y) + 1, initial=-1))[1:]
        self.build(string, end_idxes)

    # 打印后缀树
    def __repr__(self):
        def state_desc(state: State):
            if state.left is None: return "⊥"
            if state.left == -1: return self.string
            return (self.string[state.left:] if state.right == float('inf') else self.string[state.left:state.right+1]) + (" (end)" if state.right == float("inf") else "")

        def suffix_link_desc(state: State, prefix=""):
            return prefix + state_desc(state.suffix_link) if state.suffix_link else ""

        def recur(state: State, level, res):
            res += state_desc(state) + suffix_link_desc(state, prefix=" ----> ") + "\n"
            for next_state in state.transition.values():
                res += "\t" * level
                res += recur(next_state, level + 1, "")
            return res
        return recur(self.root, 0, "")

    def _update(self, active_state, left, idx):
        old_active_point = self.root
        is_end_point, split_state = self._test_and_split(active_state, left, idx - 1, self.string[idx])
        while not is_end_point:
            new_state = State(idx, float('inf'))
            split_state.transition[self.string[idx] if idx not in self.end_idxes else 'end'] = new_state
            if old_active_point != self.root:
                old_active_point.suffix_link = split_state
            old_active_point = split_state
            active_state, left = self._canonize(active_state.suffix_link, left, idx - 1)
            is_end_point, split_state = self._test_and_split(active_state, left, idx - 1, self.string[idx])
        if old_active_point != self.root:
            old_active_point.suffix_link = active_state
        return active_state, left

    def _test_and_split(self, active_state, left, right, char):
        if left > right:
            return char in active_state.transition, active_state
        next_state = active_state.transition[self.string[left]]
        next_char_idx = next_state.left + right - left + 1
        if right + 1 not in self.end_idxes and char == self.string[next_char_idx]:
            return True, active_state
        split_state = State(next_state.left, next_char_idx - 1)
        active_state.transition[self.string[left]] = split_state
        next_state.left = next_char_idx
        split_state.transition[self.string[next_char_idx]] = next_state
        return False, split_state

    def _canonize(self, active_state, left, right):
        if left > right:
            return active_state, left
        next_state = active_state.transition[self.string[left]]
        while next_state.right - next_state.left <= right - left:
            left += next_state.right - next_state.left + 1
            active_state = next_state
            if left <= right:
                next_state = active_state.transition[self.string[left]]
        return active_state, left


class Application:

    # 最长公共子串
    @staticmethod
    def lcs(string1, string2, debug=False):
        string = string1 + "$" + string2 + "$"
        tree = STree()
        tree.build_with_automatic_end([string1, string2])
        if debug: print(tree)
        
        def dfs(state: State):
            if state.right == float('inf'):
                return '', state.left >= len(string) - len(string2) - 1
            res, has_string1, has_string2 = [], False, False
            for s in state.transition.values():
                res_string, is_string2 = dfs(s)
                if len(res_string) > 0:
                    res.append((string[state.left:state.right+1] if state.left != -1 else "") + res_string)
                else:
                    if is_string2: has_string2 = True
                    else: has_string1 = True
            if has_string1 and has_string2:
                res.append(string[state.left:state.right+1])
            return max(res, key=lambda x: len(x)) if res else '', is_string2

        return dfs(tree.root)[0]

    # 最长公共子串
    @staticmethod
    def lcss(strings, debug=False):
        string = '$'.join(strings) + '$'
        str_lens = list(accumulate(strings, lambda x, y: x + len(y) + 1, initial=0))
        tree = STree()
        tree.build_with_automatic_end(strings)
        if debug: print(tree)
        
        def dfs(state: State):
            if state.right == float('inf'):
                return '', {next(i for i in range(len(str_lens) - 1) if state.left < str_lens[i + 1])}
            res, string_set = [], set()
            for s in state.transition.values():
                res_string, string_idxes = dfs(s)
                if len(res_string) > 0:
                    res.append((string[state.left:state.right+1] if state.left != -1 else "") + res_string)
                else:
                    string_set.update(string_idxes)
            if len(string_set) == len(strings):
                res.append(string[state.left:state.right+1])
            return max(res, key=lambda x: len(x)) if res else '', string_set

        return dfs(tree.root)[0]
                

if __name__ == '__main__':
    # tree = STree()
    # tree.build_with_automatic_end(["abacdacdacdbc"])
    # tree.build_with_automatic_end(["cacaocac", "ccaooc"])
    # tree.build("1234332214$")
    # tree.build("asjknx")
    # print(tree)

    # print(Application.lcs("12335665464566321", "12366546456653321"))
    # print(Application.lcs("abcd", "bcd", debug=True))
    # print(Application.lcss(["abcdfds", "bfdbcdfew", "bcdrgde"], debug=True))
    print(Application.lcss(["acacs", "caccuiesscca", "kascnnckccac", "cccjssaaacacccs"]))
    

