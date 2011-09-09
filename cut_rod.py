def cut_rod(p, n):
    """straightforward, top-down, recursive manner"""
    if n == 0:
        return 0
    q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

################################################################################

def memoized_cut_rod(p, n):
    """top-down cut-rod procedure, with memoization added"""
    
    r = [-1] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
    for i in range(1, n + 1):
        q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q

################################################################################

def bottom_up_cut_rod(p, n):
    """bottom-up dynamic-programming approach"""
    
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] +r[j - i])
        r[j] = q
    return r[n]

################################################################################

def extended_bottom_up_cut_rod(p, n):
    """bottom-up dynamic-programming approach with an actual solution"""
    
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return (r, s)

def print_cut_rod_solution(p, n):
    (r, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print s[n]
        n = n - s[n]

if __name__ == "__main__":
    p = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}
    for i in range(1, 11):
        print cut_rod(p, i)
        #print memoized_cut_rod(p, i)
        #print bottom_up_cut_rod(p, i)
    
    (r, s) = extended_bottom_up_cut_rod(p, 10)
    print r
    print s
    
    print_cut_rod_solution(p, 10)
    print_cut_rod_solution(p, 7)