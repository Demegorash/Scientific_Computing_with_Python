''' 

This will be theory.  After step 8 we need to remove it, however we are going to comment, but from 7 to begginging this was not commented.

my_list = [1,2]

my_list.append(3)
print(my_list)

print(my_list[0])

my_list[0] = 0
print(my_list)

my_list.insert(1, 1)
print(my_list)

my_list.pop()
print(my_list)

'''

def add_expense(expenses, amount, category):
    expenses.append({"amount" : amount, "category" : category})

def print_expenses(expenses):
    for expense in expenses:
        pass

expenses = []