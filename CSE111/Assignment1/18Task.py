def is_palindrome(word):
    string = ""
    for char in word:
        if char != " ":
            string += char

    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")


word = input().lower()
is_palindrome(word)