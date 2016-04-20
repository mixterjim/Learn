class Students(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_name(self):
        print(self.__name)

    def print_score(self):
        print(self.__score)

    def set_Student(self, name, score):
        self.__name = name
        self.__score = score
Jim = Students('Jim', 100)
# Jim.__name
Students.print_name(Jim)
Students.print_score(Jim)
#Ben.__name = "Ben"
Ben = Students('Ben', 66)
print(Ben._Students__name, Ben._Students__score)  # Do not use this
