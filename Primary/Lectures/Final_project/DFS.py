def dfs(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    path = []
    min_path = []

    def backtrack(current):
        nonlocal min_path
        if (current[0] < 0 or current[0] >= rows or current[1] < 0 or current[1] >= cols or
                grid[current[0]][current[1]] == 1 or tuple(current) in visited):
            return
        path.append(current)
        visited.add(tuple(current))
        if current == target:
            if not min_path or len(path) < len(min_path):
                min_path = path[:]
        else:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                new_x, new_y = current[0] + dx, current[1] + dy
                backtrack([new_x, new_y])
        path.pop()


    backtrack(start)
    return min_path if min_path else "没有找到从起点到目标点的路径"


grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start = [0, 0]
target = [3, 3]

result = dfs(grid, start, target)
print(result)