from timeit import default_timer as timer


def cut_rod(p: dict, n: int):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[str(i)] + cut_rod(p, (n - i)))
    return q


def memoized_cut_rod_aux(p: list, n: int, r: list):
    if r[n - 1] >= 0:
        return r[n - 1]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            q = max(q, p[str(i)] + memoized_cut_rod_aux(p, n - i, r))
    r[n - 1] = q
    return q


def memoized_cut_rod(p: list, n: int):
    r = [float("-inf")] * n  # solution values
    return memoized_cut_rod_aux(p, n, r)


def bottom_up_cut_rod(p: list, n: int):
    r = [0]
    for j in range(1, n+1):
        q = float("-inf")
        for i in range(1, j+1):
            q = max(q, p[str(i)] + r[j - i])
        r.append(q)
    return r[n]


def main():
    prices = {"1": 1, "2": 5, "3": 8, "4": 9, "5": 10,
              "6": 17, "7": 17, "8": 20, "9": 24, "10": 30,
              "11": 33, "12": 33, "13": 35, "14": 39, "15": 40,
              "16": 43, "17": 45, "18": 45, "19": 50, "20": 53,
              "21": 54, "22": 58, "23": 62, "24": 62, "25": 66,
              "26": 68, "27": 71, "28": 72, "29": 75, "30": 80}
    n = [5]  #, 10, 15, 20, 25, 30]
    for n in n:
        start = timer()
        opt = memoized_cut_rod(prices, n)
        end = timer()
        print("n = " + str(n) + " - Run time: " + str(end - start) + ". Optimal revenue: " + str(opt))
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
