# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", "bacon"],
#     ["egg", "spam"],
#     ["egg", "beacon", "spam"],
#     ["egg", "bacon", "sausage", "spam"],
#     ["spam", "bacon", "sausage", "spam"],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"]
# ]
#
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#     print()
#
# for meal in menu:
#     for item in range(len(meal) - 1, - 1, - 1):
#         if meal[item] == "spam":
#             del meal[item]
#     print(meal)

#
# f_num = int(input("Enter first number: "))
# s_num = int(input("Enter second number: "))
#
# for item in range(f_num, s_num):

def is_palindrome(string):
    return string[:: - 1] == string


def sentence_palindrome(string):
    new_string = ""
    for item in string:
        if item.isalnum():
            new_string += item
    print(new_string)
    return string[:: - 1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if sentence_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")