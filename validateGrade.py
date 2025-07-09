def valide_grade(grade):
    if grade >= 90:
        return "A+"
    elif grade >= 80:
        return "A"
    elif grade >= 70:
        return "B"
    elif grade >= 60:
        return "c"
    elif grade >= 50:
        return "D"
    else:
        return "F"
