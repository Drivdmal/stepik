def tribonacci(n):
    cach = {1:1, 2:1, 3:1, 4:3, 5:5}
    def recurs(n):
        result = cach.get(n)
        if result is None:
            result = recurs(n-3) + recurs(n-2) + recurs(n-1)
            cach[n] = result
        return result
    return recurs(n)

print(tribonacci(5))
