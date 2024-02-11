class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def avg_rate_course(self, course):
        sum_rating = 0
        len_rating = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        res = round(sum_rating / len_rating, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.aver_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.aver_rating() < other.aver_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def aver_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def avg_rate_course(self, course):
        sum_rating = 0
        len_rating = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        res = round(sum_rating / len_rating, 2)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.aver_rating() < other.aver_rating()


class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Студенты
best_student_1 = Student('Ruoy', 'Eman', 'Man')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ["Basic"]

best_student_2 = Student('Alex', 'Petrov', 'Man')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ["Pascal"]

# Лекторы
lecturer_1 = Lecturer('Maria', 'Ivanova')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Darya', 'Petrova')
lecturer_2.courses_attached += ['Python']

# Проверяющие
cool_reviewer_1 = Reviewer('John', 'Jonson')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Peter', 'Smith')
cool_reviewer_2.courses_attached += ['Python']

# Выставление оценок студентам
cool_reviewer_1.rate_hw(best_student_1, 'Python', 2)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 4)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 5)

cool_reviewer_2.rate_hw(best_student_2, 'Python', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 8)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 8)

# Выставление оценок лекторам
best_student_1.rate_lect(lecturer_1, 'Python', 10)
best_student_1.rate_lect(lecturer_1, 'Python', 10)
best_student_1.rate_lect(lecturer_1, 'Python', 10)

best_student_2.rate_lect(lecturer_2, 'Python', 5)
best_student_2.rate_lect(lecturer_2, 'Python', 5)
best_student_2.rate_lect(lecturer_2, 'Python', 5)

student_list = [best_student_1, best_student_2]
lecturer_list = [lecturer_1, lecturer_2]

def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.avg_rate_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating

print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
