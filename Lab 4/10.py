n = int(input("Enter a number of Fibonacci numbers to  generate: "))
fib_list = [0, 1]
for i in range(2, n):
    fib_list.append(fib_list[i-1] + fib_list[i-2])
print(fib_list)