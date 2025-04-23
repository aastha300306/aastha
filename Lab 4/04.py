n = int(input("Enter a number: "))
def prime_number(n):
    isPrime = 1
    i = 2
    if(n<=1):
        isPrime = 1
    else:
        while(i <= n/2):
            if(n%2 == 0):
                isPrime = 0
                break
            i += 1
    if(isPrime):
        print("Number is Prime number: ")
    else: 
        print("Number is not a Prime number: ")

def palindrome(n):
    n1 = str(n)
    if(n1 == n1[::-1]):
        print("Number is a palindrome: ")
    else:
        print("Number is not a palindrome: ")

palindrome(n)
prime_number(n)