def spiralOrder(matrix: list) -> list:
    if not matrix: return []
    curr = (0, -1)
    direction = (0, 1)
    visit = {}
    res = []
    def next_direction(direction):
        if direction == (0, 1): return 1, 0
        elif direction == (1, 0): return 0, -1
        elif direction == (0, -1): return -1, 0
        else: return 0, 1
    while True:
        next_position = curr[0] + direction[0], curr[1] + direction[1]
        if next_position in visit or next_position[0] < 0 or next_position[0] >= len(matrix) or next_position[1] < 0 or next_position[1] >= len(matrix[0]):
            direction = next_direction(direction)
            next_position = curr[0] + direction[0], curr[1] + direction[1]
            if next_position in visit or next_position[0] < 0 or next_position[0] >= len(matrix) or next_position[1] < 0 or next_position[1] >= len(matrix[0]):
                break
        curr = next_position
        visit[curr] = True
        res.append(matrix[curr[0]][curr[1]])
    return res

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
