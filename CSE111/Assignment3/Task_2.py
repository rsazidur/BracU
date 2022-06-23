class Course:
    def __init__(self, name, faculty, section):

        self.name = name
        self.faculty = faculty
        self.section = section

    def detail(self):
        print(self.name, "-", self.faculty, "-", self.section)


c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE111", "TBA", 9)
c2.detail()