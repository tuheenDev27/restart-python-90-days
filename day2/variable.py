'''
Create a 3 types of variable in python and perform some meaningful operations on them.

'''
def check_type(variable_1):
    if(type(variable_1) == int):
        print(variable_1 * 2)
    else:
        print(variable_1 * 7)

result = check_type("this is tuheen")

def compare_var(var1, var2):
    print(var1 > var2)
    print(var1 < var2)
    print (var1 == var2)

resulT = compare_var(10, 20)