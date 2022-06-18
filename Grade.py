# Class to get a grade between 1 and 6 with 0.5 increments

class Grade:
    getGrade: str = input("Grade of Student ")
    grade: float = float(getGrade)
    if grade == 1:
        print(grade)
    elif grade == 1.5:
        print(grade)
    elif grade == 2:
        print(grade)
    elif grade == 2.5:
        print(grade)
    elif grade == 3:
        print(grade)
    elif grade == 3.5:
        print(grade)
    elif grade == 4:
        print(grade)
    elif grade == 4.5:
        print(grade)
    elif grade == 5:
        print(grade)
    elif grade == 5.5:
        print(grade)
    elif grade == 6:
        print(grade)
    else:
        print("Error grade can not be bigger than 6! please enter valid grade")
