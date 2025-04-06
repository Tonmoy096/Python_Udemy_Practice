# Variable scope

# Global scope and local scope

global_var = 10


def my_function():  # Global variable
    print("Inside function: global_var=", global_var)


my_function()

print("Outside function: global_var=", global_var)


def local_function():  # Local variable

    local_var = 20

    print("Local variable inside function=", local_var)


local_function()


def modify_global():

    global global_var
    global_var = 30

    print("Inside function : global variabl=", global_var)


modify_global()

print("Outside function: global_var=", global_var)
