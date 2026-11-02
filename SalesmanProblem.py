
import random

cities = ['A', 'B', 'C', 'D']

dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def cost(route):
    total = 0
    for i in range(len(route)):
        total += dist[route[i]][route[(i+1) % 4]]
    return total

beam = [cities[:]]

for step in range(10):
    new = []

    for route in beam:
        for i in range(1, 4):
            r = route[:]
            r[1], r[i] = r[i], r[1]
            new.append(r)

    beam = sorted(new, key=cost)[:2]

best = min(beam, key=cost)

print("Best Route:", best + [best[0]])
print("Minimum Distance:", cost(best))
