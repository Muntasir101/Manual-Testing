def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


print(calculate_average([1, 2, 3, 4]))  # Expected output: 2.5

"""
This code will produce incorrect results because 
the division operator / performs integer division, 
and the result should be a floating-point number.
"""