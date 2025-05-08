def is_prime(n):
    if n <= 1:
        print("It is not a prime number")
        return
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            print("It is not a prime number")
            return
    print("Yes, it is a prime number")

number = int(input("Enter a number: "))
is_prime(number)
