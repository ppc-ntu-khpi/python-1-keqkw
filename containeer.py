def temperatures(C):

    F = [round(c * 9/5 + 32, 1) for c in C]
    F.reverse()
    print(F)
    
    print("Всього вимірювань:", len(F))

def checkStudentGrades(grades):
    if 2 in grades:
        print('Студент має принаймні одну двійку з дисципліни!')
    else:
        print('Студент вчиться без двійок')


def studentGrades(students):
    for student in students.keys():
        students[student] = min(students[student] + 1, 5.0)
    print(students)


def countRespondents(responses):
    respondents = set(responses)
    print("Всього респондентів:", len(respondents))


C = [10.0, 15.5, 17.1, 17.6, 19.0, 19.9, 25.0, 25.8, 28.0, 29.0, 30.1]
temperatures(C)

grades = (4, 5, 4, 4, 3, 5, 3, 3, 2, 5, 5, 5)
checkStudentGrades(grades)

students = {"Васильєв": 3.5, "Семенов": 4.0, "Петров": 4.5, "Іванов": 3.0, "Мар'їн": 5.0}
studentGrades(students)

responses = ["Іванов", "Петров", "Сидоров", "Васильєв", "Семенов", "Іванов", "Мар'їн", "Сидоров", "Дмитрієв", "Іванов"]
countRespondents(responses)
