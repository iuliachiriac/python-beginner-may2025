from string import punctuation


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


def get_words(sentence):
    punctuation_marks = ",.!?):"
    for char in punctuation_marks:
        sentence = sentence.replace(char, "")
    sentence = sentence.lower()
    words = sentence.split()
    return words


print(get_words("When we discussed Python data types, we (purposely) missed a"
                " big part of their behavior: their methods. "))
text = ("But, they are associated with objects, which means we need an object "
        "on which we call them.")
print(get_words(text))
