
file = ""
counts = dict()

for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1

big_count = None
big_word = None

for word, counts in counts.items():
    if big_count is None or counts > big_count:
        big_word = word
        big_count = counts
print(big_word, big_count)


count = 0
students = [
    ("John", ["CompSci", "Physics"]),
    ("Susi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Yuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

for (name, subject) in students:
    if "CompSci" in subject:
        count += 1
print(count)

