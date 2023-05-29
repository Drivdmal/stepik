def get_fast_pow(a, n):
    if n == 0:
        return 1
    if n%2==0:
        return get_fast_pow(a,n//2) * get_fast_pow(a,n//2)
    else:
        return get_fast_pow(a,n-1)*a


print(get_fast_pow(2,10))