def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

if __name__ == "__main__":
    p = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17,  8:20, 9:24, 10:30}
    for i in range(1, 11):
        print cut_rod(p, i)