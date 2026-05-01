def is_armstrong_number(number):
    digits_as_str = str(number)
    power = len(digits_as_str)
    
    total_sum = sum(int(digit) ** power for digit in digits_as_str)
    
    # Check if you have the word 'return' here!
    return total_sum == number