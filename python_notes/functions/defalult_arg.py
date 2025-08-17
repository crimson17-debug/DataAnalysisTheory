#default arguments in functions

# default arguments in functions are used when 
# the user does not pass any arguments.
# default arguments are values assigned to parameter in
# the function definition that functions uses to perform its code and 
# return a value.






#///////////////////problems ////////////////////////////////






# def cal_product(a=1, b=1):
#     product = a*b
#     return product


# output = cal_product()
# print(output)  # Output will be 1 since default values are used

# def len_list(lst):
#     length = len(lst)
#     return length


# output = len_list([1, 2, 3, 4, 5])
# print(output)  # Output will be 5 since the list has 5 elements


# def print_list(lst):
#     for items in lst:
#         print(items, end=" ")
    
#     return None


# print_list([1, 2, 3, 4, 5])  # Output will be 1 2 3 4 5
# print_list()  # This will raise an error since the function requires a list argument


# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# factorial(5)  # Output will be 120 since 5! = 5*4*3*2*1 = 120


# def cash_convertor(amount):
#     rupees = (amount * 85.56)
#     return rupees

# rupees = cash_convertor(100)
# print(f"Converted amount in rupees: {rupees}")  # Output will be converted amount in rupees