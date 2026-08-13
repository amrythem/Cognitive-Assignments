n = int(input("Enter a number: "))
sum = 0

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        sum = sum + num

print("Sum of prime numbers =", sum)