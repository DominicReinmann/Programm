class Subjects:
    sb = "Subject"
    subjects = input("Enter subject ")
    subject = subjects.capitalize()

    if subject == "English" or "english":
        print(f"{sb} {subject}")
    elif subject == "German" or "german":
        print(f"{sb} {subject}")
    elif subject == "French" or "french":
        print(f"{sb} {subject}")
    elif subject == "Mathematics" or "mathematics":
        print(f"{sb} {subject}")
    elif subject == "Physics" or "physics":
        print(f"{sb} {subject}")
    elif subject == "Sport" or "sport":
        print(f"{sb} {subject}")
    elif subject == "Chemistry" or "chemistry":
        (f"{sb} {subject}")
    elif subject == "Art" or "art":
        (f"{sb} {subject}")
    else:
        print("Please enter a valid Subject")
