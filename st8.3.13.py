def is_power(number):
    if number < 2:
        if number == 1:
            return True
        else:
            return False
    return True if (number * is_power(number/2)) else False
    
print(is_power(512))
