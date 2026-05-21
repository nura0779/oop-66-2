

def simple_decorator(func):
    def wrapper():
        print("До выполнения!!")
        func()
        print("после выполнения!!")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!!")

# say_hello()

# 3
def greeting_decorator(func):
    # 4
    def wrapper(name):
        print(f"{name} Привет!!") # 5
        func(name) # 6
    return wrapper # 7

@greeting_decorator #2
def greet(name):
    print(f"{name} как дела ?")

# greet("Ardager") #1

# @greeting_decorator
# def tttt(arg):

def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_decorator(5)
def hi():
    print('HI!!')
# hi()

def class_decorator(cls):
    class NewClass(cls):
        def action1(self):
            print("New action!!")
    return NewClass

# @class_decorator
class OldClass:
    def action(self):
        print('Old action!!')
test_obj = OldClass()
# test_obj.action()
# test_obj.action1()
print(type(test_obj))

# def is_admin():
#     pass
#
# @is_admin
# def ban_user(user):
#     user.is_activa = False