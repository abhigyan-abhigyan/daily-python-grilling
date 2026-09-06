def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

test_numbers = [1, 16, 3, 32, 0]
for val in test_numbers:
    print(f"Is {val} a power of two?:", is_power_of_two(val))
