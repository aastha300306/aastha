def recursive_average(numbers, total=0, count=0):
    if not numbers: 
        return total / count if count != 0 else 0
    return recursive_average(numbers[1:], total + numbers[0], count + 1)

numbers = [10, 20, 30, 40, 50]
average = recursive_average(numbers)
print("Average:", average)