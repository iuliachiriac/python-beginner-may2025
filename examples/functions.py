def my_function():
    """Prints a greeting message"""
    print('Hello world!')


def greet(name: str):  # function with type hints
    print(len(name))
    print(f"Hello, {name}!")


print(my_function)
help(my_function)

my_function()
my_function()

greet("Anna")
# greet(1)
