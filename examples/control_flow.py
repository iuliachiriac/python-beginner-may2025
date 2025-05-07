name = "Felix"
is_cat = True

if is_cat:
    print(f"{name} is a cat")
    print("is_cat is a truthy value (not necessarily a boolean)")
    print("Still under if")
else:
    print(f"{name} is not a cat")

print("Outside if")

if is_cat is True:
    print(f"{name} is a cat")
    print("is_cat is a boolean")


while True:
    sentence = input("Enter a sentence: ")

    if not sentence:
        break

    if len(sentence) < 5:
        print("Not a sentence")
        continue

    print("Sentence is:", sentence)
