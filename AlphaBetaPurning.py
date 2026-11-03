
def minimax(depth, node, maximizing, alpha, beta):

    if depth == 3:
        return tree[node]

    if maximizing:
        best = -999

        for i in range(2):
            val = minimax(depth+1, node*2+i,
                          False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best

    else:
        best = 999

        for i in range(2):
            val = minimax(depth+1, node*2+i,
                          True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best


tree = [3, 5, 6, 9, 1, 2, 0, -1]

result = minimax(0, 0, True, -999, 999)

print("Best Value:", result)
