# recursion:
# its a loop in a function
# where it calls itself

# recursion needs three things:
# 1.objective of function: what is the work of the function
# 2.function call: the function should call itself
# 3.base case: the condition that stops the recursion

# example: print numbers from n to 1

# 1. objective : to print numbers from n to 1
# def print_numbers(n) :
#     if n==0:
#         return
#     print (n) #prints the current number
# # 2. call function:
#     print_numbers(n-1) #calls the function with n-1 so now n is initialized to n-1
# # 3. base case:
    

# print_numbers(5)

# example: factorial of a number
def fact(n):
    if n ==0 or n==1:
        return 1
    else:
        return fact(n-1)*n
    
    
ouptput = fact(5)
print(ouptput)  # Output will be 120 since 5! = 5*4*3*2*1 = 120


def calc_sum(n):
    if n==0:
        return 0
    else:
        return calc_sum(n-1) + n
    
output = calc_sum(5)
print(output)  # Output will be 15 since 5+4+3+2+1 = 15
    

def call_lst(lst, index=0):
    if index == len(lst):
        return
    else:
        print(lst[index], end=" ")
        call_lst(lst, index + 1)

call_lst([1, 2, 3, 4, 5])  # Output will be 1 2 3 4 5 each on a new line
print(end="\n")  #this prints new line since the end is now not a space and its a new line character
print(output)
print(end=None)
print(output)
print(output - 2)
print(output + 12)


