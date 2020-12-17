class Node:
    def __init__(self, start, end=None, suffix_link=None):
        self.children = {}
        self.start = start
        self.end = end
        self.suffix_link = suffix_link

    @property
    def length(self):
        return self.end - self.start if self.end else None

    @property
    def is_leaf(self):
        return self.length is None


class SuffixTree:
    def __init__(self, data):
        self.data = data
        self.root = Node(0)
        self.root.suffix_link = self.root

        # 活动点三元组
        self.active_node = self.root
        self.active_edge = None
        self.active_length = 0
        # 剩余后缀数
        self.remainder = 0

    # 打印后缀树
    def __repr__(self):
        res = ""
        def node_desc(node: Node):
            return self.data[node.start:node.end] if node.length else self.data[node.start:]
        def recur(node: Node, level):
            nonlocal res
            res += node_desc(node) + "\n"
            for child in node.children.values():
                res += "\t" * level
                recur(child, level + 1)
        recur(self.root, 0)
        return res

    def build(self):
        idx = 0
        last_split_node = None

        while idx < len(self.data):
            char = self.data[idx]

            if self.active_edge is None:  # active_edge 为空，则找不找得到都不会 split
                if char in self.active_node.children:  # 找到了 char
                    node = self.active_node.children[char]
                    self.active_edge = char
                else:  # 没找到，所以创建 node  (Rule 3)
                    node = Node(idx, suffix_link=self.root)
                    self.active_node.children[char] = node
                    self.active_node = self.active_node.suffix_link
                    last_split_node = None
                    idx += 1
                    continue
            else:
                node = self.active_node.children[self.active_edge]
                next_idx = node.start + self.active_length
                if char != self.data[next_idx]:  # 没找到，所以 split
                    node.end = next_idx
                    node.children[self.data[next_idx]] = Node(next_idx, suffix_link=self.root)
                    node.children[char] = Node(idx, suffix_link=self.root)
                    if last_split_node is not None:
                        last_split_node.suffix_link = node
                    last_split_node = node
                    self.active_node = self.active_node.suffix_link
                    if self.active_length == self.remainder:
                        self.active_edge = None if self.remainder == 1 else self.data[idx - self.remainder + 1]
                        self.active_length -= 1
                    self.remainder -= 1
                    continue

            if not node.is_leaf and node.length == self.active_length + 1:  # 走到新的结点
                self.active_node = node
                self.active_edge = None
                self.active_length = 0
            else:  # 没走到新的结点，就往前走一步
                self.active_length += 1
            
            self.remainder += 1
            idx += 1


if __name__ == "__main__":
    st = SuffixTree("abcabxabdbd$")
    st.build()
    print(st)
