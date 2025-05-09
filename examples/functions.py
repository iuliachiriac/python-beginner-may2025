def my_function():
    """Prints a greeting message"""
    print('Hello world!')


def greet(name: str):  # function with type hints
    print(f"Hello, {name}!")


def get_words(sentence):
    punctuation_marks = ",.!?):"
    for char in punctuation_marks:
        sentence = sentence.replace(char, "")
    sentence = sentence.lower()
    words = sentence.split()
    return words


print("__name__ in functions.py =", __name__)

if __name__ == "__main__":  # if current module is executed (not imported)
    print(my_function)
    help(my_function)

    my_function()
    my_function()

    greet("Anna")
    # greet(1)

    print(get_words("When we discussed Python data types, we (purposely) "
                    "missed a big part of their behavior: their methods. "))
    text = ("But, they are associated with objects, which means we need an "
            "object on which we call them.")
    print(get_words(text))
