import numpy as np


def optimal_bst(p, q, n):
    e = np.zeros((n + 1, n))
    w = np.zeros((n + 1, n))
    root = np.zeros((n, n))
    for i in range(n + 1):
        e[i, i - 1] = q[i - 1]
        w[i, i - 1] = q[i - 1]
    for l in range(1, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            e[i, j] = float('inf')
            w[i, j] = w[i, j - 1] + p[j] + q[j]
            for r in range(i, j+1):
                t = e[i, r - 1] + e[r + 1, j] + w[i, j]
                if t < e[i, j]:
                    e[i, j] = t
                    root[i, j] = r
    return e[1:len(e)], root[1:len(root)]


def main():
    p = np.array([0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14])
    q = np.array([0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05])

    p2 = np.array([0, 0.15, 0.1, 0.05, 0.1, 0.20])
    q2 = np.array([0.05, 0.10, 0.05, 0.05, 0.05, 0.10])

    e, root = optimal_bst(p2, q2, len(q2))

    print(e)
    print(root)


if __name__ == '__main__':
    main()
