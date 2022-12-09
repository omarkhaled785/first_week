def sum_of_digit(n):
    sum=0
    while n!=0:
        sum =sum +(n%10)
        n=n//10
    return sum   

num =int(input("Enter the number between 1,1000: "))

if num<0 or num>1000:
    print("worng input")
    exit()
x= sum_of_digit(num)%2
print(x!=0)

