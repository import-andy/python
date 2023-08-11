# Passing Arguments to the function:
    # 1. by value (simple types, doesn't affect Globally, new variable assigned)
    # 2. by reference (complex types, affects Globally, old variable modified)

salary = 2000
expense = 700
name = 'James'
interest_rate = 0.04

# 1. Argument passing by value (simple, will not affect).
# It's when changes made to the value of the Local variable did'n change the value of the Global varibale.
def print_savings_detais(name, salary, expense, interest_rate):     
    print('Name of account:', name)
    expense = expense + 100  # This was added. 'expense' on the right side was taken from Global, and assigned to Local 'expense'
    savings = salary - expense
    print('Savings:', savings)
    print('Interest rate:', interest_rate)

print_savings_detais(name, salary, expense, interest_rate)          # Argument 'expense' was passed by value
print()                                                             # Local 'expense' was changed, but not the Global

# 2. Argument passing by reference (complex, will affect).
# It's when changes to the variables inside the function WILL AFFECT that variable outside the function.
# It only refers to a complex data types like lists, tuples, dicts, etc.:
fruits_list = ['mango', 'banana', 'apple', 'pear']
print('Before the function:', fruits_list)

def change_list(fruits_list):
    fruits_list[0] = 'kiwi'                        # Redefining the element in a Global list
    print('Inside the function:', fruits_list)

change_list(fruits_list)
print('After the function:', fruits_list)
print()

# Another example with dict:
car_speed_dictionary = {'Camry' : 120, 'Accord' : 130, 'Cayenne' : 1250, 'Mini Cooper' : 100}
print('Before the function:', car_speed_dictionary)

def change_dictionary(some_dictionary):                      # Check out, that input arg is not 'car_speed_dictionary'
    some_dictionary['Camry'] = 140
    print('Inside the function:', car_speed_dictionary)

change_dictionary(car_speed_dictionary)
print('After the function:', car_speed_dictionary)
