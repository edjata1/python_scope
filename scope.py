
print("-----------global scope----------------")
# global scope
name = "Empress"
count = 1

def greeting():
    #local scope
    color = "red"
    # called inside function
    print(color)
    # local scope, using global scope 'name'
    print(name)

greeting()

print()
print("--------------- local scope ---------------------")

def greeting(firstname):
    #local scope
    color = "pink"
    # called inside function access to local scope
    print(color)
    # access to global scope
    print(name)
    print(firstname)

# argument 'Enid'
greeting("Enid")
print()

# using global scope 'name'
greeting(name)

print("--------------- local scope ---------------------")

# function parameter 'name'
def greeting(name):
    #local scope
    color = "pink"
    # called inside function access to local scope
    print(color)
    # access to local scope from parameter
    print(name)

# argument 'Enid'
greeting("Enid")
print()

# using global scope 'name'
greeting(name)

print()
print("--------------- function scope ---------------------")

def another():
    # local scope called another function changed parameter "name"
    greeting("Timmy")

another()

print()
print("------ Nested Functions ------------")

def one_function():
     
    color = 'purple'

    # nested function
    # define function inside another function
    def inside_another_function(name):
        
        print(color)
        print(name)
    inside_another_function("Mike")

one_function()
print()

print("--------------- Modify variable from global variable ---------------------")
# modify assignment of variable inside function using global varible

def one_function():
     
    color = 'purple'
    # local variable not from global
    count = 2
    print(count)

    # nested function
    # define function inside another function
    def inside_another_function(name):
        
        print(color)
        print(name)
    inside_another_function("Mike")

one_function()
print()


def one_function():
     
    color = 'purple'
    # creating another variable in local scope
    # count += 1 # won't work right undefine local variable

    # add to global count
    global count
    # modify global value
    count += 1
    # acess from global variable 'count'    
    print(count)

    # nested function
    # define function inside another function
    def inside_another_function(name):
        # use color from parent function
        nonlocal color
        color = "Green"
        
        print(color)
        print(name)
    inside_another_function("Mike")

one_function()
print()