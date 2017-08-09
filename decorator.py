def say_hi():
    print("Hi, there!")

# A decorator function extends the function of other functions
def decorator(func):
    def wrap():
        print("++++")
        func()
    return wrap
    # return a function and call it

decorated_hi = decorator(say_hi)
decorated_hi()

# The same can be done with the decorator @
@decorator
def say_hello():
    print ('Hello')

say_hello()