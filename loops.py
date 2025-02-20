# # sum of even numbers
# even_sum = 0
# for number in range(2, 11,2):
#     # print(number)
#     even_sum += number
# print(even_sum)
#
#
# # sum off odd numbers
# n=(int(input("Enter a number: ")))
# sum=0
# for i in range(1,n+1):
#     if(i%2!=0):
#         sum=sum+i
# print(sum)


# # sum of even numbers
# n=(int(input("Enter a number: ")))
# sum=0
# for i in range(2,n+1):
#
#     if (i%2==0):
#         sum=sum+i
# print(sum)


# sum of prime numbers
def sum_of_primes(num):
    sum=0
    for i in range(2,11,2):
        if num%i==0:
            sum=sum+i
print(sum)