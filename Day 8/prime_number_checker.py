def prime_number(a):
    count = 0
    for i in range(1,a+1):
        if(a%i == 0):
            count +=1
    if(count == 2):
        print("It is a prime number.")
    else:
        print("It is not a prime number.")

num = int(input("Enter a number: "))
prime_number(num)
