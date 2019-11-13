
# def fun_name(param_1 ... param_n):
#    pass
#
#
#def 
# functions can have parameters 
# functions can have default params with values but on the rt side
# functions can be called and invoked with names 
# functions can be aliased 
# functions params if having defualts not requied to pass thos value
# function params can be called by named parameters (sequence is not required)
# function names should be always snake_case 
# function parameters should be always snake_case 
# function can return values , functions , objects ---> 
# functions should have documenatation as the first  line 
# functions need to be always defined with small letters no caps
# functions can support variable args  
# function can support named dictionary args 

def calculate_profits(total_cost, sale_price):
    print(sale_price-total_cost)

def calculate_tax(total_cost, sale_price, tax=10):
    print(sale_price-total_cost)

#normal invocation
calculate_profits(1,2)
#invocation with default values
calculate_tax(1,2)
# named  parameter invocation
calculate_profits(sale_price=10, total_cost=20)
calculate_tax(192,9283)
# alias the function
calculate_my_tax = calculate_tax
calculate_my_tax()




