class Buttons:
    def __init__(self, word, spaces, border):
        self.word = word
        self.spaces = spaces
        self.border = border

        print(f"{self.word} Button Specifications:")
        print(f"Button name: {self.word}")
        print(f"Number of the border characters for the top and the bottom: {self.border}")
        print(f"Number of spaces between the left side border and the first character of the button name: {self.spaces}")
        print(f"Number of spaces between the right side border and the last character of the button name: {self.spaces}")
        print(f"Characters representing the borders: {self.border}")



word = "CANCEL"
spaces = 10
border = 'x'
b1 = Buttons(word, spaces, border)
print("=======================================================")
b2 = Buttons("Notify", 3, '!')
print("=======================================================")
b3 = Buttons('SAVE PROGRESS', 5, '$')