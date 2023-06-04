def linear(nested_lists):
    l = []
    for n in nested_lists:
        if type(n) == int:
            l.append(n)
        else:
            l += linear(n)
    return l

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(linear(my_list))
        
