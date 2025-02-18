def count_adjacent_mines(grid, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x]) and grid[x + dx][y + dy] == "*":
                count += 1
    return count

field_num = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    field_num += 1
    if field_num > 1:
        print()
    print(f"Field #{field_num}:")
    grid = [input().strip() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "*":
                print("*", end="")
            else:
                count = count_adjacent_mines(grid, i, j)
                print(count, end="")
        print()

