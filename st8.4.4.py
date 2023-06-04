def recursive_sum(nested_lists):
    count = 0
    for n in nested_lists:
        if type(n) == int:
            count += n
        else:
            count += recursive_sum(n)
    return count 

print(recursive_sum([1, [4, 4], 2, [1, [2, 10]]]))
