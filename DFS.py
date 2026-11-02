
def dfs(a, b, visited):
    if (a, b) in visited:
        return False

    visited.add((a, b))
    print(a, b)

    if a == 2:
        return True

    # Fill jug A
    if dfs(4, b, visited):
        return True

    # Fill jug B
    if dfs(a, 3, visited):
        return True

    # Empty jug A
    if dfs(0, b, visited):
        return True

    # Empty jug B
    if dfs(a, 0, visited):
        return True

    # Pour A into B
    x = min(a, 3-b)
    if dfs(a-x, b+x, visited):
        return True

    # Pour B into A
    x = min(b, 4-a)
    if dfs(a+x, b-x, visited):
        return True

    return False


visited = set()
print("Jug A  Jug B")
dfs(0, 0, visited)
