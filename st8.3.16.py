from sys import argv

def to_binary(number):
    if number <= 1:
        return str(number)
    var = number // 2
    return to_binary(var) + str(number - var*2) 

print(to_binary(int(argv[1])))
